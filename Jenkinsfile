@Library('jenkins-shared-lib') _

pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                script {
                    try {
                        gitClone('https://github.com/myuser/myrepo.git', 'main')
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
                        buildImage('flask-docker-app', 'v1')
                    } catch (e) {
                        error("❌ Stage Docker Build failed: ${e.message}")
                    }
                }
            }
        }

        stage('Run Docker') {
            steps {
                script {
                    try {
                        deployApp('flask-docker-app', 'v1')
                    } catch (e) {
                        error("❌ Stage Docker Run failed: ${e.message}")
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
