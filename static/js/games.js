//Base url for deployed app
//baseurl= 'http://harryforskitt.com:5000';

console.log("js run");

//Base url for local development
baseurl= 'http://127.0.0.1:5000/';

function makeGame(){
    var name = document.getElementById('name').value
    var password = document.getElementById('password').value
	url=baseurl.concat("/makegame/").concat(name).concat("/").concat(password);
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		console.log(data);
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
};

function getGames(){
    var name = document.getElementById('name').value
    var password = document.getElementById('password').value
	url=baseurl.concat("/getgames");
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		console.log(data);
        document.getElementById("games").innerHTML = data;
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
};

getGames();