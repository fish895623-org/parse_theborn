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
        stage('testing dockerfile') {
          agent { dockerfile true }
          steps {
            sh 'echo working well?'
            sh 'chmod +x chromedriver'
          }
        }
      }
    }
  }
}