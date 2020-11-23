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
                sh 'cd technoatom-2020-2/lection10/code/tests/'
                dir('technoatom-2020-2/lection10/code/tests/') {
                    sh "pytest -s -l -v test_base.py --alluredir=$WORKSPACE/allure-results"
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