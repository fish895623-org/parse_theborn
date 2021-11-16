pipeline {
  agent none
  stages {
    stage('Testing') {
      agent any
      steps {
        sh "ls -alh"
        sh "echo abcd"
      }
    }
    stage('test2') {
      stages {
        stage('testing dockerfile') {
          agent { dockerfile true }
          steps {
            sh 'echo working well?'
            sh 'pwd'
            sh 'uname -a'
          }
        }
      }
    }
  }
}