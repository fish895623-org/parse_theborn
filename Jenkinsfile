pipeline {
  agent none
  stages {
    stage('Testing') {
      agent any
      steps {
        sh "ls -alh"
      }
    }
    stage('test2') {
      stages {
        stage('Chromedriver executable') {
          agent { dockerfile true }
          steps {
            sh 'echo working well?'
            sh 'chmod +x chromedriver'
          }
        }
        stage('launch main.py') {
          agent { dockerfile true }
          steps {
            sh 'python3 src/main.py'
            sh 'ls -alh'
          }
        }
      }
    }
  }
}