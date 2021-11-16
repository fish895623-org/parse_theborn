pipeline {
  agent none
  stages {
    stage('Chromedriver executable') {
      agent any
      steps {
        sh 'time docker image build --no-cache .'
      }
    }
//     stage('launch main.py') {
//       agent { dockerfile true }
//       steps {
//         sh 'chmod 755 chromedriver'
//         sh 'python3 src/main.py'
//         sh 'ls -alh'
//       }
//     }
  }
}