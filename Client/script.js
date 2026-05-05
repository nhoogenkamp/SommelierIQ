//https://stackoverflow.com/questions/57891275/simple-fetch-get-request-in-javascript-to-a-flask-server 

// display in table :https://www.youtube.com/watch?v=eS-FVnhjvEQ

function getWines() {
    const url = 'http://localhost:8080/getWines'
    fetch(url)
    .then(response => response.json())  
    .then(json => {

        let out = "";

        json.forEach(element => {
            out += `
                <tr>
                    <td>${element.year}</td>
                    <td>${element.name}</td>
                    <td>${element.wine_type}</td>
                    <td>${element.grape}</td>
                    <td>${element.country}</td>
                    <td>${element.region}</td>
                    <td>${element.price}</td>
                </tr>
            `;            
        });
        document.getElementById("demo").innerHTML = out;
    })
}