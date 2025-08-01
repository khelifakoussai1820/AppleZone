const iconPassword = document.getElementById("iconPassword");
const passwordField = document.getElementById("password");

iconPassword.addEventListener("click", function () {
    const isHidden = passwordField.type === "password";
    passwordField.type = isHidden ? "text" : "password";


    iconPassword.classList.add("animate-icon");


    if (isHidden) {
        iconPassword.classList.remove("fa-eye");
        iconPassword.classList.add("fa-eye-slash");
    } else {
        iconPassword.classList.remove("fa-eye-slash");
        iconPassword.classList.add("fa-eye");
    }

    // Enlève l'animation après un court délai
    setTimeout(() => {
        iconPassword.classList.remove("animate-icon");
    }, 300);
});
