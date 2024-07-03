
// Fetch the items from the JSON file
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}


// main
loadItems()
    .then(items => {
    //    displayItems(items);
    //    setEventLisners(items)
    })
    .catch(console.log);