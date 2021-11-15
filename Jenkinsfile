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
        sh 'echo 잘되냐'
      }
    }
  }
}