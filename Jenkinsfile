pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'cd C:\\Users\\samiksha vaidya\\PycharmProjects\\SeleniumAutomation && pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'cd C:\\Users\\samiksha vaidya\\PycharmProjects\\SeleniumAutomation && pytest'
            }
        }
    }
}