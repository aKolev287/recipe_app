function main(){
  const header = document.querySelector(".nav-container");
  const toggleClass = "sticky";
  
  document.addEventListener("scroll", () => {
    const currentScroll = document.documentElement.scrollTop;
    if (currentScroll > 150) {
      header.classList.add(toggleClass);
    } else {
      header.classList.remove(toggleClass);
    }
  });
}
main();

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

