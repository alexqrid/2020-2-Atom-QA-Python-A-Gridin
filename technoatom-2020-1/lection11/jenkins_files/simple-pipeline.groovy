properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        timestamps()
    }

    stages {

        stage("Build") {
            steps {
                echo 'building..'
                echo 'build done!'
            }
        }

        stage("Testing") {
            steps {
                sh 'cd lection11/code/tests/'
                dir('lection11/code/tests/') {
                    sh "pytest -s -l -v test_simple.py --alluredir=$WORKSPACE/allure-results"
                }
            }
        }
    }

    post {
        always {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: '$WORKSPACE/allure-results']]
            ])
        }
    }
}