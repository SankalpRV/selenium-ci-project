pipeline {
    agent {
        docker {
            image 'python:3.12'
        }
    }

    stages {
        stage('Check Python Version') {
            steps {
                sh 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Test Only') {
            steps {
                sh 'pytest tests/test_math.py'
            }
        }
    }
}