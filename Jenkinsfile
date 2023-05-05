pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * *')
    }
    stages {
        stage('Unit test') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
}
