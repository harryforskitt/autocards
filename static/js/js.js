function getRandomInt(max) {
	return Math.floor(Math.random() * max);
}

//Base url for deployed app
//baseurl= 'http://harryforskitt.com:5000'

//Base url for local development
baseurl= 'http://127.0.0.1:5000/';

console.log('js.js');

function displayPlayerCard(){
	url=baseurl.concat("/playercard/0");
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		data=data.split(",");
		console.log(data);
		document.getElementById("pcname").innerHTML = data[0];
		document.getElementById("pcdpsec").innerHTML = data[2];
		document.getElementById("pcdpshot").innerHTML = data[3];
		document.getElementById("pcfirerate").innerHTML = data[4];
		document.getElementById("pcmagsize").innerHTML = data[5];
		document.getElementById("pcrating").innerHTML = data[6];
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
};

function displayComputerCard(){
	url=baseurl.concat("/playercard/1");
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		data=data.split(",");
		document.getElementById("ccname").innerHTML = data[0];
		document.getElementById("ccdpsec").innerHTML = data[2];
		document.getElementById("ccdpshot").innerHTML = data[3];
		document.getElementById("ccfirerate").innerHTML = data[4];
		document.getElementById("ccmagsize").innerHTML = data[5];
		document.getElementById("ccrating").innerHTML = data[6];
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
};
	
function playCard(attribute, player){
	displayComputerCard();
	console.log("playcard")
	url=baseurl.concat("/play/").concat(attribute).concat("/").concat(player);
	console.log(url)
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		console.log("Data: ".concat(data));
		if (data == "computer"){
			document.getElementById("winner").innerHTML = "Computer's Turn!";
		}
		else{
			document.getElementById("winner").innerHTML = "Your Turn!";
		}
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
	displayPlayerCard();
	computerCards();
	playerCards();
};

function computerPlay(){
	displayComputerCard();
	var player = '1';
	var attribute = getRandomInt(5);
	url=baseurl.concat("/play/").concat(attribute).concat("/").concat(player);
	console.log(url);
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (adata) {
		// This is the JSON from our response
		console.log("Data: ".concat(adata));
		if (adata == "computer"){
			document.getElementById("winner").innerHTML = "Computer's Turn!";
		}
		else{
			document.getElementById("winner").innerHTML = "Your Turn!";
		}
		return(adata);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
	computerCards();
	playerCards();
};

function playerCards(){
	var player = '0';
	var attribute = getRandomInt(5);
	url=baseurl.concat("/playercards/0");
	console.log(url)
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		console.log(data);
		document.getElementById("playerCards").innerHTML = data;
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
};

function computerCards(){
	var player = '0';
	var attribute = getRandomInt(5);
	url=baseurl.concat("/playercards/1");
	console.log(url)
	fetch(url).then(function (response) {
		// The API call was successful!
		return response.text();
	}).then(function (data) {
		// This is the JSON from our response
		console.log(data);
		document.getElementById("computerCards").innerHTML = data;
		return(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	})
};

displayPlayerCard();
computerCards();
playerCards();