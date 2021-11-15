pipeline {
  agent none
  stages {
    stage('Testing') {
      agent any
      steps {
        // Testing
        checkout scm
        sh "ls -alh"
        sh "echo abcd
            echo twooooo"
      }
    }
  }
}