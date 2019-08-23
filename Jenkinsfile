pipeline {
  agent any

  tools {nodejs "node"}

  stages {

    stage('Cloning Git') {
      steps {
        git 'https://github.com/spaceflightnewsapi/spaceflightnewsapi.git'
      }
    }

    stage('Install dependencies') {
      steps {
        sh 'npm install'
      }
    }

    stage('Test') {
        steps {
            withCredentials([string(credentialsId: 'Mongo Credentials SNAPI (RO)', variable: 'mongo_uri')]) {
                sh 'MONGODB_URI=$mongo_uri npm test'
            }
        }
    }
  }
}
