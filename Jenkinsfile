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
                echo 'Docker push will be configured using Jenkins Credentials.'
            }
        }
    }
}