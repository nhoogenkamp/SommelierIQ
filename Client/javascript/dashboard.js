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
});
}