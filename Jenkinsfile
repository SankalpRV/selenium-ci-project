pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests in Parallel') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        bat 'python -m pytest tests/test_math.py'
                    }
                }
                stage('Selenium Tests') {
                    steps {
                        bat 'python -m pytest tests/test_first.py'
                    }
                }
            }
        }
    }
}