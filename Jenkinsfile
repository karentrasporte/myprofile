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

        stage('Build and Push to Docker Hub') {
            steps {
                echo 'Building and pushing multi-platform image...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker buildx create --use || true"
                    sh "docker buildx build --platform linux/amd64,linux/arm64 -t ${IMAGE_NAME}:${IMAGE_TAG} --push ."
                }
            }
        }

        stage('Deploy to Droplet') {
            steps {
                echo 'Deploying to Digital Ocean Droplet...'
                sshagent(['droplet-ssh']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no root@${DROPLET_IP} '
                            docker pull ${IMAGE_NAME}:${IMAGE_TAG} &&
                            docker stop my-profile || true &&
                            docker rm my-profile || true &&
                            docker run -d -p 5000:5000 --name my-profile ${IMAGE_NAME}:${IMAGE_TAG}
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