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

        stage('Lint') {
            steps {
                echo '🔍 Running Python lint with flake8...'
                sh '''
                    pip install flake8
                    flake8 . --exit-zero --count --statistics --show-source --max-line-length=100
                '''
            }
        }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo 🔐 Logging in to Docker Hub
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME
                        docker logout
                    '''
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
}
