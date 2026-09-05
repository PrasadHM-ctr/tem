pipeline {
    agent any

    environment {
        KUBECONFIG = 'C:\\Users\\bhuva\\.kube\\config'
        DOCKER_IMAGE = 'prasadhm4454/temperature-converter'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t temperature-converter:%BUILD_NUMBER% .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-prasad',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    bat 'echo %DOCKER_PASSWORD% | docker login --username %DOCKER_USERNAME% --password-stdin'

                    bat 'docker tag temperature-converter:%BUILD_NUMBER% %DOCKER_IMAGE%:%BUILD_NUMBER%'

                    bat 'docker push %DOCKER_IMAGE%:%BUILD_NUMBER%'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl set image deployment/temperature-converter temperature-converter=%DOCKER_IMAGE%:%BUILD_NUMBER%'

                bat 'kubectl rollout status deployment/temperature-converter'
            }
        }

    }
}