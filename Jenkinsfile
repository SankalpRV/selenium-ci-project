pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest test_math.py'
            }
        }
    }
}