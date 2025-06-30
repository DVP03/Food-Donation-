import { RecaptchaVerifier, signInWithPhoneNumber } from "firebase/auth";
import { auth } from './firebase';

// Initialize reCAPTCHA
window.recaptchaVerifier = new RecaptchaVerifier('recaptcha-container', {
  'size': 'invisible',
  'callback': response => {
    console.log("reCAPTCHA solved");
  }
}, auth);

// Send OTP
signInWithPhoneNumber(auth, phoneNumber, window.recaptchaVerifier)
  .then(confirmationResult => {
    window.confirmationResult = confirmationResult;
    console.log("OTP sent!");
  })
  .catch(error => console.error("SMS not sent", error));

// Verify OTP
window.confirmationResult.confirm(code)
  .then(result => {
    console.log("Phone auth success:", result.user);
  })
  .catch(error => console.error("OTP verification failed", error));
