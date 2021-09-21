function showDetails(evt, details) {
    var i, x, tablinks;;
    var x = document.getElementsByClassName("details");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
    }
    document.getElementById(details).style.display = "block";
    evt.currentTarget.className += " w3-red";
}
