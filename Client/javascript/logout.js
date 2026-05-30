function logoutAdmin() {
    fetch(`https://sommelieriq-production.up.railway.app/logout`, {
        method: "POST",
        credentials: "include"
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(json) {
        console.log(json);

        window.location.href = "/Client/pages/login.html";
    });
}