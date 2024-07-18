function sortidea() {
    const sorting = document.getElementById('sorting').value;
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set('so', sorting);
    window.location.search = urlParams.toString();
}