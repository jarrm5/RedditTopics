var API_KEY = "";
var SEARCH_ENGINE_ID = "";
var ENDPOINT = "https://www.googleapis.com/customsearch/v1?";

$(document).ready(function(){

    $('#btn-reset').on('click', function(){
        $('#inp-topic').val('');
    });

	$('#btn-search').on('click',function(){
        var input = $('#inp-topic').val();
        if(input === ""){
            alert('Please enter something');
        }
        else{
            //Need to get csv parsing results here
            pythonParseRedditThreads(input);
            //sendHTTPRequest(input);
        }
    });

    function pythonParseRedditThreads(keyword){
        $.ajax({
            type: 'POST',
            url: '../python/SortingTopics.py',
            data: { param: keyword },
        }).done(function(result){
            console.log('script succesfully executed.');
            console.log(result);
        }).fail(function(){
            console.log('Failed to load SortingTopics.py');
        });
        
    }
    
    function sendHTTPRequest(query){
        $.ajax({
          type: 'GET',
          dataType: 'json',
          url: ENDPOINT + 'key=' + API_KEY + '&cx=' + SEARCH_ENGINE_ID + '&q=' + query
        }).done(function(response) {
            if(response.queries.request.count == 0){
                console.log("No results found.");
            }
            else{
                for (var i = 0; i < 10; i++) {
                    var imageURL = response.items[i].pagemap.cse_image[0].src;
                    console.log(imageURL);
                }
            }
        }).fail(function() {
            console.log('HTTP call failed.');
        });
    }
});
