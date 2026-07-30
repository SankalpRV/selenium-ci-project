pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Use Secret') {
            steps {
                withCredentials([string(credentialsId: 'demo-secret', variable: 'MY_SECRET')]) {
                    bat 'echo Secret is injected'
                    bat 'echo %MY_SECRET%'
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests'
            }
        }
    }
}