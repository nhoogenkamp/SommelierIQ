const navbarPath =
    window.location.pathname.includes("/pages/")
    ? "../components/navbar.html"
    : "./components/navbar.html";

fetch(navbarPath)
.then(response => response.text())
.then(data => {
    document.getElementById("navbar").innerHTML = data;
});