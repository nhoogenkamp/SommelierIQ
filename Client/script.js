//https://stackoverflow.com/questions/57891275/simple-fetch-get-request-in-javascript-to-a-flask-server 

// display in table :https://www.youtube.com/watch?v=eS-FVnhjvEQ

// grouping wines in colour and country; https://www.tutorialspoint.com/article/json-group-object-in-javascript

function getWines() {
    const url = 'http://localhost:8080/getWines'
    fetch(url)
    .then(response => response.json())  
    .then(json => {

        const grouped = json.reduce((groups, wine) => {

            const colour = wine.wine_type;
            const country = wine.country;

            if (!groups[colour]) {
                groups[colour] = {};
            }

            if (!groups[colour][country]) {
                groups[colour][country] = [];
            }

            groups[colour][country].push(wine);

            return groups;

        }, {});

        let out = "";

        json.forEach(element => {
            out += `
                <tr>
                    <td>${element.year}</td>
                    <td>${element.bottle_type}</td>
                    <td>${element.name}</td>
                    <td>${element.wine_type}</td>
                    <td>${element.grape}</td>
                    <td>${element.country}</td>
                    <td>${element.region}</td>
                    <td>${element.price}</td>
                </tr>
            `;            
        });
        document.getElementById("wines").innerHTML = out;
    })
}