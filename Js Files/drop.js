document.querySelector('.dropbtn').addEventListener('mouseover', function() {
    document.querySelector('.dropdown-content').classList.add('show');
});

document.querySelector('.dropdown').addEventListener('mouseleave', function() {
    document.querySelector('.dropdown-content').classList.remove('show');
});
