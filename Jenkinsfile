pipeline {
  agent any

  tools {nodejs "node"}

  stages {

    stage('Install dependencies') {
      steps {
        sh 'npm install'
      }
    }

    stage('Test') {
        steps {
            withCredentials([
              string(credentialsId: 'MONGODB_URI', variable: 'mongo_uri'),
              string(credentialsId: 'SECRET', variable: 'secret'),
              string(credentialsId: 'TESTPASS', variable: 'testpass'),
              string(credentialsId: 'TESTUSER', variable: 'testuser'),
              ]) {
                sh 'TESTUSER=$testuser TESTPASS=$testpass SECRET=$secret MONGODB_URI=$mongo_uri npm run test'
            }
        }
    }
  }
}
