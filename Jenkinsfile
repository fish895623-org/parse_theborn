pipeline {
  agent none
  stages {
    stage('Testing') {
      agent any
      steps {
        // Testing
        checkout scm
        sh "ls -alh"
        sh "echo abcd"
      }
    }
    stage('test2') {
      agent { dockerfile true }
      stages {
        stage('testing dockerfile') {
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