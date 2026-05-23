//https://stackoverflow.com/questions/57891275/simple-fetch-get-request-in-javascript-to-a-flask-server 

// display in table :https://www.youtube.com/watch?v=eS-FVnhjvEQ

function filterWines(wines) {
    const wine_id = document.getElementById("wine_id").value;
    const selectedColour = document.getElementById("wineColour").value;
    const selectedBottle = document.getElementById("bottleType").value;
    const maxPrice = document.getElementById("maxPrice").value;

    return wines.filter(wine => {

        return (
            (selectedColour === "" || wine.wine_type === selectedColour) &&
            (selectedBottle === "" || wine.bottle_type === selectedBottle) &&
            (wine_id === "" || Number(wine.wine_id) === Number(wine_id)) &&
            (maxPrice === "" || Number(wine.price) <= Number(maxPrice))
        );

    });
}

function getWines() {
    document.getElementById("wineSection").style.display = "block";
    const url = 'http://localhost:8080/getWines'
    fetch(url)
    .then(response => response.json())  
    .then(json => {

    const filteredWines = filterWines(json);

    let out = "";

    filteredWines.forEach(element => {
        out += `
            <tr>
                <td>${element.wine_id}</td>
                <td>${element.year}</td>
                <td>${element.bottle_type}</td>
                <td>${element.name}</td>
                <td>${element.wine_type}</td>
                <td>${element.grape}</td>
                <td>${element.country}</td>
                <td>${element.region}</td>
                <td>${element.price}</td>
                <td>${element.body_score}</td>
                <td>${element.tannin_score}</td>
                <td>${element.acidity_score}</td>
                <td>${element.sweetness_score}</td>
                <td>${element.description}</td>
            </tr>
        `;
    });

    document.getElementById("wines").innerHTML = out;
    document.getElementById("Wineform").reset();
});
}
function closeWines() {

    document.getElementById("wineSection").style.display = "none";

}

// same style as login
function addWine() {
    
    // getting values from html and us this to sent to Flask backend
    var entry = {
        restaurant_id: document.getElementById("restaurant_id").value,
        name: document.getElementById("name").value,
        wine_type: document.getElementById("wine_type").value,
        grape: document.getElementById("grape").value,
        country: document.getElementById("country").value,
        region: document.getElementById("region").value,
        year: document.getElementById("year").value,
        bottle_type: document.getElementById("bottle_type").value,
        price: document.getElementById("price").value,
        available: document.getElementById("available").value,
        description: document.getElementById("description").value,
        body_score: document.getElementById("body_score").value,
        tannin_score: document.getElementById("tannin_score").value,
        acidity_score: document.getElementById("acidity_score").value,
        sweetness_score: document.getElementById("sweetness_score").value
    };


     // Send POST request to Flask backend with method, body preventing browser from caching and telling flask its JSON data
    fetch(`http://localhost:8080/addWine`, {
        method: "POST",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

    // Check response from Flask
    .then(function(response) {
        if (response.status !==200) {
            console.log(`response status was not 200: ${response.status}`);
            document.getElementById("addWineForm").reset();
            return response.json();
        }
        console.log("received new wine")
        // had to return in order to use the next .then function
        return response.json()
    })

    .then(function(json) {
        console.log(json);
        document.getElementById("addMessage").innerHTML = json.message || json.error;

        if(json.message){
            // clearing fields
            document.getElementById("addWineForm").reset();
        }

    });

}

// Delete 1 wine with popup: https://www.w3schools.com/js/js_popup.asp
function deleteWine() {
    var entry = {
        wine_id: document.getElementById("delete_wine_id").value,
        };
    console.log(entry.wine_id);    

    if (confirm(`Please confirm you want to delete wine ID ${entry.wine_id}`)) {
        document.getElementById("deleteMessage").innerHTML =  "Deleting wine";

        // Send POST request to Flask backend with method, body preventing browser from caching and telling flask its JSON data
        fetch(`http://localhost:8080/deleteWine`, {
            method: "POST",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })

        // Check response from Flask
        .then(function(response) {
            if (response.status !==200) {
                console.log(`response status was not 200: ${response.status}`);
                return response.json();
            }
            console.log("Deleted wine")
            // had to return in order to use the next .then function
            return response.json()
        })

        .then(function(json) {
            console.log(json);
            document.getElementById("deleteMessage").innerHTML = json.message || json.error;

            if(json.message){
                // clearing fields
                document.getElementById("deleteWineForm").reset();
            }
            if(json.error){
            // clearing fields
            document.getElementById("deleteWineForm").reset();
        }
        });
    } else {
        document.getElementById("deleteMessage").innerHTML = "You pressed Cancel!";
    }      

}
function updateWine() {
    var entry = {
        wine_id: document.getElementById("update_wine_id").value,
        price: document.getElementById("update_price").value,
        };  

        // Send POST request to Flask backend with method, body preventing browser from caching and telling flask its JSON data
        fetch(`http://localhost:8080/updateWine`, {
            method: "POST",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })

        // Check response from Flask
        .then(function(response) {
            if (response.status !==200) {
                console.log(`response status was not 200: ${response.status}`);
                return response.json();
            }
            console.log("updated wine price")
            // had to return in order to use the next .then function
            return response.json()
        })

        .then(function(json) {
            console.log(json);
            document.getElementById("updateMessage").innerHTML = json.message || json.error;

            if(json.message){
                // clearing fields
                document.getElementById("updateWineForm").reset();
            }
            if(json.error){
            // clearing fields
            document.getElementById("updateWineForm").reset();
        }
    });   

}