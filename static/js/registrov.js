
function validateForm() {
    
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;
    if (password != confirmPassword) {
        document.getElementById("error-message").innerHTML = "Contraseña no coincide.";
        
        return false;
    }   else {
        // login failed
        
    }
    
}  