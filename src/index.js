import {initializeApp} from 'firebase/app';
import {getAuth, onAuthStateChanged} from 'firebase/auth';
import {getFirestore} from 'firebase/firestore';
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
    apiKey: "AIzaSyBTESduo16ELE-QFjv8Q3RZkY9gRXJJPEk",
    authDomain: "ec463-miniproject-aae95.firebaseapp.com",
    projectId: "ec463-miniproject-aae95",
    storageBucket: "ec463-miniproject-aae95.appspot.com",
    messagingSenderId: "1015457778417",
    appId: "1:1015457778417:web:7e91098d71011edb63b750",
    measurementId: "G-1EBW7CQLVS"
  };

const firebaseApp = initializeApp(firebaseConfig);
const analytics = getAnalytics(firebaseApp);
const auth = getAuth(firebaseApp);
const db = getFirestore(firebaseApp);

console.log('Hello there, Firestore!');