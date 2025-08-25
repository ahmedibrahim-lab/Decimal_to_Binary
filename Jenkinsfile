pipeline {
    agent any

    triggers {
        githubPush()
    }
    environment {
        PYTHON = '/usr/bin/python3'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python app...'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}