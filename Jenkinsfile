@Library('jenkins-shared-lib') _

pipeline {
    agent any

    stages {

        stage('Clear Workspace') {
            steps {
                cleanWs()
            }
        }
        
        stage('Git Clone') {
            steps {
                script {
                    try {
                        gitClone('https://github.com/devopsboy666/pipeline-share-lib.git', 'main')
                    } catch (e) {
                        error("❌ Stage Git Clone failed: ${e.message}")
                    }
                }
            }
        }

        stage('Build Docker') {
            steps {
                script {
                    try {
                        buildImage('flask-docker-app', 'v1', 'pipeline-share-lib')
                    } catch (e) {
                        error("❌ Stage Docker Build failed: ${e.message}")
                    }
                }
            }
        }

    }

    post {
        failure {
            echo "📛 Pipeline failed!"
        }
        success {
            echo "✅ Pipeline completed successfully!"
        }
    }
}
