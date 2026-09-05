pipeline {
    agent any

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
                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                    
                    bat 'docker tag temperature-converter:%BUILD_NUMBER% %DOCKER_USERNAME%/temperature-converter:%BUILD_NUMBER%'
                    
                    bat 'docker push %DOCKER_USERNAME%/temperature-converter:%BUILD_NUMBER%'
                }
            }
        }
    }
}