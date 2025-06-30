import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";
import { auth } from './firebase';

// Sign Up
createUserWithEmailAndPassword(auth, email, password)
  .then(userCredential => {
    console.log("Signed up:", userCredential.user);
  })
  .catch(error => console.error(error));

// Sign In
signInWithEmailAndPassword(auth, email, password)
  .then(userCredential => {
    console.log("Signed in:", userCredential.user);
  })
  .catch(error => console.error(error));
