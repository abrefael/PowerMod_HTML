

var data={};
data['m_or_n'] = 'norm';
data['keep_data'] = 'yes';
var audio;
var hints = [];
var results = '';
var N = 1;
var i;
var j;
var folder_path = "http://localhost:8889/Put_Media_Files_in_Here/";
var responses = 5;

function buildTable(n_rows){
	var tbl_content = '';
	var tbl = document.getElementById("file_table");
	const NUMBERING = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth'];
	N = n_rows;
	console.log(N);
	tbl_content += '<tr><colgroup><col span="1" style="width: 30%;">' +
		'<col span="1" style="width: 25%;">' +
		'<col span="1" style="width: 45%;">' +
		'</colgroup><th>Usage</th><th>File name</th>' +
		'<th>Preview</th></tr>';
	for (i=0; i < n_rows; i++){
		let I = String(i+1);
		tbl_content +='<tr><td>' + NUMBERING[i] + ' scene\'s video file</td>';
		tbl_content +='<td><button onclick="file_select(\'vid\',' + I + ',0)">Select File</button></td>';
		tbl_content +='<td id="vid_' + I + '_0"></td></tr>';
		tbl_content +='<tr><td>' + NUMBERING[i] + ' scene\'s image file</td>';
		tbl_content +='<td><button onclick="file_select(\'img\',' + I + ',0)">Select File</button></td>';
		tbl_content +='<td id="img_' + I + '_0"></td></tr>';
		for (j=0; j < responses; j++){
			let J = String(j+1);
			if (j == 3){
				tbl_content +='<tr><td>' + NUMBERING[i] + ' scene\'s audio hint</td>';
				tbl_content +='<td id="aud_' + I + '"><button onclick="file_select(\'aud\',' + I + ',0)">Select File</button></td>';
				tbl_content +='<td><button onclick="playAudio(hints[' + String(i) + '])" type="button">Play Hint</button>';
				tbl_content +='<button onclick="pauseAudio()" type="button">Pause Hint</button> </td></tr>';
			}
			else if (j == 4){
				tbl_content +='<tr><td>' + NUMBERING[i] + ' scene\'s text hint</td>';
				tbl_content +='<td colspan="2"><textarea id="text_hint_' + I + '"></textarea></td></tr>';
			}
			else{
				tbl_content +='<tr><td>' + NUMBERING[i] + ' scene\'s ' + NUMBERING[j].toLowerCase() + ' response\'s video file</td>';
				tbl_content +='<td><button onclick="file_select(\'vid\',' + I + ',' + J +')">Select File</button></td>';
				tbl_content +='<td id="vid_' + I + '_' + J + '"></td></tr>';
				tbl_content +='<tr><td>' + NUMBERING[i] + ' scene\'s ' + NUMBERING[j].toLowerCase() + ' response\'s image file</td>';
				tbl_content +='<td><button onclick="file_select(\'img\',' + I + ',' + J +')">Select File</button></td>';
				tbl_content +='<td id="img_' + I + '_' + J + '"></td></tr>';
			}
		}
	}
	tbl.innerHTML = tbl_content;
}

function playAudio(aud_path){
	audio = new Audio(aud_path);
	audio.play();
}

function pauseAudio() {
	audio.pause();
}

function file_select(f_tp,k,n) {
	var elem = f_tp + '_' + String(k) + '_' + String(n);
	var accept_lst = '';
	if (f_tp == 'vid'){
		accept_lst = "video/mp4, video/webm, video/3gpp, video/ogg, video/x-msvideo";
	}
	else if (f_tp == 'img'){
		accept_lst = 'image/png, image/jpg, image/jpeg, image/gif, image/webp, image/bmp';
	}
	else {
		accept_lst = 'audio/mpeg, audio/ogg, audio/aac, audio/flac, audio/3gpp';
	}
	var input = document.createElement('input');
	input.accept = accept_lst;
	input.type = 'file';
	input.onchange = e => {
		var file = e.target.files[0];
		var file_path = folder_path + file.name;
		data[f_tp + '_' + k + '_' + n] = file.name;
		var x;
		if (f_tp == 'vid'){
			x = document.createElement("VIDEO");
			x.setAttribute("src", file_path);
			x.setAttribute("width", "80%");
			x.setAttribute("controls", "controls");
			let el = document.getElementById(elem);
			if (el.hasChildNodes()) {
				el.removeChild(el.children[0]);
			}
			el.appendChild(x);
		}
		else if (f_tp == 'img'){
			x = document.createElement("img");
			x.src = file_path;
			x.style.width = '80%';
			let el = document.getElementById(elem);
			if (el.hasChildNodes()) {
				el.removeChild(el.children[0]);
			}
			el.appendChild(x);
		}
		else {
			hints[Number(k)-1] = file_path;
			document.getElementById('aud_' + k).innerHTML = 
				'<button onclick="file_select(\'aud\',' +
				k + ',0)">Select File</button> File selected:' + 
				' <p style="color: blue;">' +
				 file_path + '</p>'
		}
	}
	input.click();
}


function go(){
	var hint_texts = document.querySelectorAll('textarea');
	if (hint_texts.length > 0){
		for (let k=0; k < hint_texts.length; k++) {
			let hint_text = hint_texts[k];
			data[hint_text.id] = hint_text.value;
		}
	}
	data['N'] = N;
	fetch('http://localhost:8889/data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	})
	.then(response => response.text())
	.then(result => console.log(result))
	.catch(error => console.error('Error:', error));
}


