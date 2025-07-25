pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
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
