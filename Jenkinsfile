pipeline {
  agent none
  stages {
    stage('Chromedriver executable') {
      agent any
      steps {
        sh 'docker build -t parse -f Dockerfile .'
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