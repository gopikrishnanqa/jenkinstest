pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                echo '🧹 Cleaning old workspace'
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/gopikrishnanqa/jenkinstest'
            }
        }

        stage('Verify Workspace') {
            steps {
                echo '🔍 Checking workspace contents...'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'echo 🚧 Building Docker image'
                sh 'docker version'
                sh 'docker build -t jgkgopi/fastapi-app:6 .'
            }
        }
    }
}
