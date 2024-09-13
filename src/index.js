import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyBTESduo16ELE-QFjv8Q3RZkY9gRXJJPEk",
    authDomain: "ec463-miniproject-aae95.firebaseapp.com",
    projectId: "ec463-miniproject-aae95",
    storageBucket: "ec463-miniproject-aae95.appspot.com",
    messagingSenderId: "1015457778417",
    appId: "1:1015457778417:web:7e91098d71011edb63b750",
    measurementId: "G-1EBW7CQLVS"
  };

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

window.db = db;
window.auth = auth;

console.log("Firestore initialized:", db);