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

        stage('Lint Modified Files') {
            steps {
                echo '🔍 Running flake8 on modified Python files...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install flake8

                    # Find modified *.py files compared to main branch
                    CHANGED_FILES=$(git diff --name-only origin/main...HEAD -- '*.py')

                    if [ -z "$CHANGED_FILES" ]; then
                        echo "✅ No Python file changes detected."
                    else
                        echo "🔍 Linting the following Python files:"
                        echo "$CHANGED_FILES"
                        flake8 $CHANGED_FILES --count --statistics --show-source --max-line-length=100
                    fi
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
