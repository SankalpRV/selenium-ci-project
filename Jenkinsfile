pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests --junitxml=report.xml --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}