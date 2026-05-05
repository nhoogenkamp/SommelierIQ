function getWines() {
    const url = 'http://localhost:8080/getWines'
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
        document.getElementById("demo").innerHTML = JSON.stringify(json)
    })
}