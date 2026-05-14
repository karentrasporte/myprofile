pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'karentrasporte'
        IMAGE_NAME = 'karentrasporte/my-profile'
        IMAGE_TAG = 'latest'
        DROPLET_IP = '188.166.253.218'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy to Droplet') {
            steps {
                echo 'Deploying to Digital Ocean Droplet...'
                sshagent(['droplet-ssh']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no root@${DROPLET_IP} '
                            cd /root/my-profile && \
                            git pull origin main && \
                            docker build -t my-profile:latest . && \
                            docker stop my-profile || true && \
                            docker rm my-profile || true && \
                            docker run -d -p 4000:4000 --name my-profile my-profile:latest
                        '
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed! Site is live on Digital Ocean.'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}