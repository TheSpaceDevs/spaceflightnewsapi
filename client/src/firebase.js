// import firebase from 'firebase';
import firebase from 'firebase/app';
import 'firebase/firestore';

const config = {
  projectId: 'spaceflightnewsapi-80573',
};
firebase.initializeApp(config);


export default firebase;