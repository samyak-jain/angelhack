import firebase from 'firebase/app';
import 'firebase/firestore';

let config = {
    apiKey: "AIzaSyDQU6cOKjJsLchvsqzwelgVP2VWNe0fU1w",
    authDomain: "angelhack-123.firebaseapp.com",
    databaseURL: "https://angelhack-123.firebaseio.com",
    projectId: "angelhack-123",
    storageBucket: "angelhack-123.appspot.com",
    messagingSenderId: "560405194520"
};
firebase.initializeApp(config);

let db = firebase.firestore();
db.settings({timestampsInSnapshots: true});

export default db;