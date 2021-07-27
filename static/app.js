let currentLocation = document.location.pathname;
let navLinks = document.querySelectorAll('.nav-item .nav-link');

function toggleActiveClass(path){
    for(let i = 0; i < navLinks.length; i++){
        if(navLinks[i].classList.contains('active')){
            navLinks[i].classList.remove('active');
        };
    }

    for(let i=0; i < navLinks.length; i++){
        if(navLinks[i].href.slice(21) == path){
            navLinks[i].classList.add('active')
        }
    }
}

window.onload = e => {
    e.preventDefault();
    $('.loader-wrapper').fadeOut('slow');
}
toggleActiveClass(currentLocation)