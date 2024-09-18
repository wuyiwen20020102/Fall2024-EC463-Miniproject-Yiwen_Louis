import { collection, addDoc } from "firebase/firestore";
import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

const signUpBtn = document.getElementById("signUp");
const firstForm = document.getElementById("form1");

firstForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = firstForm.querySelector("input[type='email']").value;
  const password = firstForm.querySelector("input[type='password']").value;
  const username = firstForm.querySelector("input[type='text']").value;

  try {
    const userCredential = await createUserWithEmailAndPassword(window.auth, email, password);

    await addDoc(collection(window.db, "username-email-pwd"), {
      uid: userCredential.user.uid,
      username: username,
      email: email
    });

    console.log("User created and saved in Firestore");
  } catch (error) {
    console.error("Error during sign-up:", error);
    alert(`Sign-up failed: ${error.message}`);
  }
});

const signInBtn = document.getElementById("signIn");
const secondForm = document.getElementById("form2");

secondForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = secondForm.querySelector("input[type='email']").value;
  const password = secondForm.querySelector("input[type='password']").value;

  try {
    const userCredential = await signInWithEmailAndPassword(window.auth, email, password);
    console.log("User signed in:", userCredential.user);
    window.location.href = "/dashboard.html";
  } catch (error) {
    console.error("Error during sign-in:", error);
    alert(`Sign-in failed: ${error.message}`);
  }
});

const container = document.querySelector(".container");

signInBtn.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});