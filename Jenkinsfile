pipeline {
    agent any

    // triggers {
    //     pollSCM('H/5 * * * *')
    // }
    stages {
        stage('Unit test') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
}
