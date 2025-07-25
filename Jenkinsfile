// Jenkinsfile
// This defines a Declarative Pipeline for a FastAPI application

pipeline {
    // Agent: Use 'any' to allow Jenkins to pick an available agent,
    // or specify a label if you have dedicated agents (e.g., 'agent { label 'docker-enabled' }').
    // The 'docker' agent will be used for specific stages.
    agent any

    // Environment variables for the pipeline
    environment {
        // Replace with your Docker Hub username or private registry URL
        DOCKER_REGISTRY = 'docker.io' // Or your private registry URL, e.g., 'myregistry.com'
        DOCKER_HUB_USERNAME = 'jgkgopi' // Your Docker Hub username
        // The ID of the Jenkins credential you created for Docker Hub/Registry
        DOCKER_CREDENTIAL_ID = 'docker-hub-credentials'
        // Name of the Docker image
        IMAGE_NAME = "fastapi-app"
    }

    stages {
        // Stage 1: Checkout the source code from Git
        stage('Checkout Source') {
            steps {
                script {
                    // Clean workspace before checkout to ensure a fresh build
                    echo "Cleaning workspace..."
                    deleteDir()
                    echo "Checking out source code..."
                    // Checkout the SCM configured in the job
                    checkout scm
                    echo "Source code checked out successfully."
                }
            }
        }

        // Stage 2: Build the Docker image
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    // Build the Docker image using the Dockerfile in the current directory.
                    // The 'docker.build' step is provided by the Docker Pipeline plugin.
                    // It tags the image with the build number and 'latest'.
                    // The 'returnStatus: true' ensures the build doesn't fail the pipeline immediately
                    // if the Docker build command itself returns a non-zero exit code.
                    def appImage = docker.build("${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}")
                    appImage.addTag("latest")
                    echo "Docker image ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER} and latest built successfully."
                }
            }
        }

        // Stage 3: Run Tests inside the Docker container
        stage('Run Tests') {
            // Use the newly built Docker image as the agent for this stage
            // This ensures tests run in an isolated and consistent environment
            agent {
                docker {
                    image "${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    // Optional: If your tests need to access services on the host or other containers,
                    // you might need to specify network configuration.
                    // args '-v /tmp:/tmp' // Example: Mount a volume if needed for test output
                }
            }
            steps {
                script {
                    echo "Running tests inside the Docker container..."
                    // Execute pytest. Ensure pytest and httpx are in your requirements.txt
                    // The 'sh' step runs a shell command inside the Docker container.
                    sh 'pytest test_main.py'
                    echo "Tests completed successfully."
                }
            }
        }

        // Stage 4: Push Docker Image to Registry
        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image to ${DOCKER_REGISTRY}..."
                    // Use 'docker.withRegistry' to authenticate with the Docker registry.
                    // It uses the credentials defined by DOCKER_CREDENTIAL_ID.
                    docker.withRegistry("https://${DOCKER_REGISTRY}", DOCKER_CREDENTIAL_ID) {
                        // Get the image that was built in the previous stage
                        def appImage = docker.image("${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}")
                        // Push both the build-numbered tag and the 'latest' tag
                        appImage.push()
                        appImage.push('latest')
                        echo "Docker image pushed to ${DOCKER_REGISTRY} successfully."
                    }
                }
            }
        }

        // Stage 5: (Optional) Cleanup
        stage('Cleanup') {
            steps {
                script {
                    echo "Cleaning up workspace..."
                    cleanWs() // Cleans the Jenkins workspace directory
                    echo "Workspace cleaned."
                    // Optional: Remove the Docker image locally after pushing
                    // sh "docker rmi ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    // sh "docker rmi ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest"
                }
            }
        }
    }

    // Post-build actions (e.g., send notifications)
    post {
        always {
            // Always run this block, regardless of build status
            echo "Pipeline finished. Status: ${currentBuild.result}"
        }
        success {
            // Run only if the pipeline succeeds
            echo "Pipeline succeeded! Image: ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
        }
        failure {
            // Run only if the pipeline fails
            echo "Pipeline failed! Check logs for errors."
            // You could add email notifications, Slack messages, etc. here
        }
        // Add more post-conditions like 'unstable', 'aborted', 'fixed', 'regression'
    }
}
