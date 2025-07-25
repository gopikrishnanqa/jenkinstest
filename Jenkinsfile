pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jgkgopi/fastapi-app:${BUILD_NUMBER}'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                echo '🧹 Cleaning old workspace'
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                echo '📥 Checking out Git repository...'
                checkout scm
            }
        }

        stage('Verify Workspace') {
            steps {
                echo '🔍 Checking workspace contents...'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Lint') {
            steps {
                echo '🔍 Running Python lint with flake8...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install flake8
                    flake8 . --count --statistics --show-source --max-line-length=100
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed!'
        }
        success {
            echo '✅ All good!'
        }
    }
}
