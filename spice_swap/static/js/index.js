function loginPassword(){
  let login_password = document.querySelectorAll("input#id_password")
  if (login_password[0].type === "password") {
    login_password[0].type = "text";
  } else {
    login_password[0].type = "password";
  }

}
function registerPassword(){
  let signup_password = document.querySelectorAll("input#id_password1");
  let confirm_passowrd = document.querySelectorAll("input#id_password2");
  if (signup_password[0].type === "password") {
    signup_password[0].type = "text";
  } else {
    signup_password[0].type = "password";
  }
  if (confirm_passowrd[0].type === "password") {
    confirm_passowrd[0].type = "text";
  } else {
    confirm_passowrd[0].type = "password";
  }
}


document.querySelector('.small-headers a').addEventListener('click', function (e) {
  e.preventDefault(); // Prevent default link behavior
  
  // Get the target section's position
  const targetSection = document.querySelector('#highest-rated');
  const targetPosition = targetSection.offsetTop;
  
  // Scroll smoothly to the target position
  window.scrollTo({
      top: targetPosition,
      behavior: 'smooth'
  });
});