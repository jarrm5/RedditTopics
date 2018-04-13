var API_KEY = "";
var SEARCH_ENGINE_ID = "";
var ENDPOINT = "https://www.googleapis.com/customsearch/v1?";

sendHTTPRequest(API_KEY,SEARCH_ENGINE_ID,ENDPOINT,'fireworks');

function sendHTTPRequest(endpoint, apiKey, searchEngineId, query){
    console.log(query);
    var url = endpoint + 'key=' + apiKey + '&cx=' + searchEngineId + '&q=' + query + '&callback=handleHTTPResponse';
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET',url,true);
    xhttp.send();
}

function handleHTTPResponse(response){
    for (var i = 0; i < response.items.length; i++) {
        var item = response.items[i];
        console.log(item);
    }
}