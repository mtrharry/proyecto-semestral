
function login(){
  document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username === "harry" && password === "1234") {
       
        window.location="../index/index.html"
    }  else {
        // login failed
        document.getElementById("error-message").innerHTML = "Usuario no registrado.";
    }
});
  
  
}

