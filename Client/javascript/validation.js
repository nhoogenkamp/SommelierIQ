function validateLogin(username, password) {

    if (username === "") {
        document.getElementById("message").innerHTML =
            "Please provide your username";
        return false;
    }
    if (password === "") {
        document.getElementById("message").innerHTML =
            "Please provide a password";
        return false;
    }
    return true;
}