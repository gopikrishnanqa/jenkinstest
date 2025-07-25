pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                echo '🧹 Cleaning old workspace'
                deleteDir()  // Wipes workspace
            }
        }
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Verify Workspace') {
            steps {
                echo '🔍 Checking workspace contents...'
                sh 'pwd'         // shows current directory
                sh 'ls -la'      // lists files in workspace
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'ls -l'  // confirm files exist
                sh 'docker build -t jgkgopi/fastapi-app:6 .'
            }
        }
    }
}
