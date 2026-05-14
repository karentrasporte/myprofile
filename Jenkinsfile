pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linter...'
                sh 'pip install flake8 && flake8 app/ --max-line-length=100'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pip install pytest && pytest tests/'
            }
        }

        stage('Build Docker image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t profile-site .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}