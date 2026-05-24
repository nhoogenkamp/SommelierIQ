// https://www.w3schools.com/js/tryit.asp?filename=tryjs_validation_number
// regex only digits: https://uibakery.io/regex-library/numbers-only

// LOGIN PAGE
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

// REGISTRATION PAGE
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

// DASHBOARD PAGE
function validatefilters(wine_id) {

    if (wine_id !== "" && !/^\d+$/.test(wine_id)) {
        document.getElementById("filtermessage").innerHTML =
            "Please provide a numerical ID or leave blank for search all wines";
        return false;
    }

    return true;
}

function validateAddWine(restaurant_id, name, wine_type, grape,country, region, year, bottle_type, price, available,description, body_score, tannin_score, acidity_score, sweetness_score) {

    const currentyear = new Date().getFullYear();

    if (restaurant_id === ""|| restaurant_id < 1 || !/^\d+$/.test(restaurant_id)) {
        document.getElementById("addMessage").innerHTML =
            "Please provide correct restaurant ID";
        return false;
    }
    if (name === "") {
        document.getElementById("addMessage").innerHTML =
            "Please provide a wine name";
        return false;
    }
        if (wine_type === "") {
        document.getElementById("addMessage").innerHTML =
            "Please provide a wine type";
        return false;
    }
        if (grape === "" || !/^[a-zA-Z\s]+$/.test(grape)) {
        document.getElementById("addMessage").innerHTML =
            "Please provide the grape";
        return false;
    }
    if (country === "" || !/^[a-zA-Z\s]+$/.test(country)) {
        document.getElementById("addMessage").innerHTML =
            "Please provide the country";
        return false;
    }
    if (region === "" || !/^[a-zA-Z\s]+$/.test(region)) {
        document.getElementById("addMessage").innerHTML =
            "Please provide the Region";
        return false;
    }
    if (year === ""|| year < 1900 || year > currentyear || !/^\d+$/.test(year)) {
        document.getElementById("addMessage").innerHTML =
            `Please provide a year between 1900 and ${currentyear}`;
        return false;
    }
    if (bottle_type === "") {
        document.getElementById("addMessage").innerHTML =
            "Please provide a bottle type";
        return false;
    }
    if (price === ""|| price < 1 || !/^\d+(\.\d{1,2})?$/.test(price)) {
        document.getElementById("addMessage").innerHTML =
            "Please provide valid price (example: 10.50 or 10)";
        return false;
    }    
    if (Number(available) !== 0 && Number(available) !== 1) {
        document.getElementById("addMessage").innerHTML =
            "Must either be available or Not available";
        return false;
    }    
    if (description.trim().split(/\s+/).length < 5) {
        document.getElementById("addMessage").innerHTML =
            "Description must have at least 5 words";
        return false;
    }
    // validation for scores
    var scores = [
        body_score,
        tannin_score,
        acidity_score,
        sweetness_score
    ];

    for (let i = 0; i < scores.length; i++) {

        if (
            scores[i] === "" ||
            !/^\d+$/.test(scores[i]) || Number(scores[i]) < 1 || Number(scores[i]) > 20
        ) {
            document.getElementById("addMessage").innerHTML =
                "Scores must be whole numbers between 1 and 20";
            return false;
    }
}
    return true;
}

function validatedeletion(wine_id) {

    if (wine_id == "" && !/^\d+$/.test(wine_id)) {
        document.getElementById("deleteMessage").innerHTML =
            "Please provide a numerical ID or leave blank for search all wines";
        return false;
    }

    return true;
}

function validatePriceUpdateWine(wine_id, price) {

    if (wine_id == "" && !/^\d+$/.test(wine_id)) {
        document.getElementById("updateMessage").innerHTML =
            "Please provide a numerical ID or leave blank for search all wines";
        return false;
    }
    if (price === ""|| price < 1 || !/^\d+(\.\d{1,2})?$/.test(price)) {
        document.getElementById("updateMessage").innerHTML =
            "Please provide valid price (example: 10.50 or 10)";
        return false;
    }  

    return true;
}

function validateAvailableUpdateWine(wine_id, available) {

    if (wine_id == "" && !/^\d+$/.test(wine_id)) {
        document.getElementById("availableMessage").innerHTML =
            "Please provide a numerical ID or leave blank for search all wines";
        return false;
    }
    if (Number(available) !== 0 && Number(available) !== 1) {
        document.getElementById("availableMessage").innerHTML =
            "Must either be available or Not available";
        return false;
    }    
    return true;
}

// VALIDATING FOOD PAIRING
function validatedishes(dishCount) {

    if (Number(dishCount) <1 || Number(dishCount) >8) {
        document.getElementById("dishMessage").innerHTML =
            "Please pick at least one dish";
        return false;
    }   
    return true;
}