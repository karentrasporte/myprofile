pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linter...'
                sh """
                    docker run --rm -v \$(pwd):/workspace -w /workspace python:3.12-slim \
                    sh -c 'pip install flake8 --quiet && flake8 app/ --max-line-length=100'
                """
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh """
                    docker run --rm -v \$(pwd):/workspace -w /workspace python:3.12-slim \
                    sh -c 'pip install flask pytest --quiet && pytest tests/'
                """
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