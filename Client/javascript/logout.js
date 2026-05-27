function logoutAdmin() {
    fetch(`http://localhost:8080/logout`, {
        method: "POST",
        credentials: "include"
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(json) {
        console.log(json);
        // redirect to dashboard page    
        window.location.href = "login.html";
    });
}
