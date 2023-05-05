pipeline {
    agent any

    stages {
        stage('Unit test'){
            steps {
                // sh "python3 test_calculator.py"
                sh "echo \"print('Hello World from Python3')\" > hello.py"
                sh "python3 hello.py"
            }
        }
    }
}