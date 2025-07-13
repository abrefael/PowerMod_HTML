var text = '';
var q=0;
var filename;

function get_participant_num(){
	//text = prompt("אנא הכניסו שם/מספר משתתף");
	//filename = text + '.csv';
	text += ',' + get_the_date() + '{br}';
}

function next_page(q_or_a){
	answers=[];
	document.getElementById('page_' + q + q_or_a).remove();
	text += getNow() + ',clicked next screen{br}';
	if (q_or_a == 'a') {
		if (q < N){
			q_or_a = 'q';
		}
		else{
			text += getNow() + ',completed{br}';
			//downloadData(text,filename);
			if (window.navigator.userAgent.indexOf("Win") != -1) {
				location.replace('/done/Done.html');
			}
			else {
				location.replace('done/Done.html');
			}
		}
		q++;
	}
	else{
		q_or_a = 'a';
	}
	document.getElementById('page_' + q + q_or_a).style.display='block';
}
function choose_answer(elem){
	var images = document.getElementsByTagName("img");
	for(var i = 0; i < images.length; i++) {
		images[i].style.borderColor = "#000000";
	}
	elem.style.borderColor = "#ff0000";
	text += getNow() + ',' + elem.id + "selected{br}";
	document.getElementById("check" + q).style.display = 'block';
}

function get_the_date(){
	var date = new Date();
	var the_date = date.toLocaleString('en-GB')
	return the_date;
}


function downloadData(data, filename) {
	var element = document.createElement('a');
	element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data));
	element.setAttribute('download', filename);
	element.style.display = 'none';
	document.body.appendChild(element);
	element.click();
	document.body.removeChild(element);
}


function getNow() {
	var date = new Date();
	current_time = date.toLocaleString('en-US', {
		hour12: false,
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
	})
	return current_time
}

