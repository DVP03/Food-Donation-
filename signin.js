import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { auth } from './firebase';

const provider = new GoogleAuthProvider();

signInWithPopup(auth, provider)
  .then(result => {
    console.log("Google sign-in successful:", result.user);
  })
  .catch(error => console.error(error));
