pipeline {
    agent any

    stages {
        stage('Run Inside Docker') {
            steps {
                script {
                    docker.image('python:3.12').inside {
                        sh 'python --version'
                        sh 'pip install -r requirements.txt'
                        sh 'pytest tests/test_math.py'
                    }
                }
            }
        }
    }
}