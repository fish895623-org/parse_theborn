pipeline {
  agent none
  stages {
    stage('test2') {
      stages {
        stage('Chromedriver executable') {
          agent { dockerfile true }
          steps {
            sh 'echo working well?'
          }
        }
        stage('launch main.py') {
          agent { dockerfile true }
          steps {
            sh 'chmod 755 chromedriver'
            sh 'python3 src/main.py'
            sh 'ls -alh'
          }
        }
      }
    }
  }
}