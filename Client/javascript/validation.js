// https://www.w3schools.com/js/tryit.asp?filename=tryjs_validation_number
// regex only digits: https://uibakery.io/regex-library/numbers-only

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

function validateRegistration(restaurant_id,username, password) {

    if (restaurant_id === ""|| restaurant_id < 1 || !/^\d+$/.test(restaurant_id)) {
        document.getElementById("message").innerHTML =
            "Please provide correct restaurant ID";
        return false;
    }
    if (username === "") {
        document.getElementById("message").innerHTML =
            "Please provide your username";
        return false;
    }
    // regex for spaces: https://stackoverflow.com/questions/980448/what-is-does-the-regular-expression-s-do
    if ( username.trim().length <6 || /\s/.test(username)) {
        document.getElementById("message").innerHTML =
            "Username needs at least 6 Characters and no spaces!";
        return false;
    }
    if (password === "" || /\s/.test(password)) {
        document.getElementById("message").innerHTML =
            "Please provide a password without any spaces";
        return false;
    }
    // regex for password: https://www.geeksforgeeks.org/javascript/javascript-program-to-validate-password-using-regular-expressions/
    if ( !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,15}$/.test(password)) {
        document.getElementById("message").innerHTML =
            "Please ensure password has one lowercase, one uppercase, one special character and minimum 8 characters long ";
        return false;
    }
    return true;
}

function validatefilters(wine_id) {

    if (wine_id !== "" && !/^\d+$/.test(wine_id)) {
        document.getElementById("filtermessage").innerHTML =
            "Please provide a numerical ID or leave blank for search all wines";
        return false;
    }
    
    return true;
}