import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import os
from tkinter import messagebox
import shutil
import glob
cwd = os.path.dirname(os.path.realpath(__file__))
d = os.path.join(cwd, 'languages')
languages = glob.glob1(d,"*.json")

ROOT = tk.Tk()
ROOT.withdraw()

def select_lang():
	msg = f'''
What laguage will you be using\n'''
	for i in range(len(languages)):
		msg += f'''
			{i+1}\t{languages[i].split('.')[0]}\n
		'''
	msg += 'Enter a number:'
	n = int(simpledialog.askinteger(title="Language", prompt=msg))
	if n > len(languages) or n < 1:
		messagebox.showinfo(title='Oops...', message='Wrong number')
		n = select_lang()
	return open(os.path.join(d,languages[n-1]),'r').read()

#dictionary = eval(select_lang())


msg = '''
עלינו לבחור תקייה בתוכה ייכנסו כל הדברים שנצטרך
'''
messagebox.showinfo(title='תקייה', message=msg)
dest_dir = filedialog.askdirectory()
dest_dir = dest_dir.replace('/','\\')
def cpit(d):
	try:
		shutil.copytree(os.path.join(cwd, d), os.path.join(dest_dir, d))
	except:
		pass

def file_collector(i, type):
	str_arr = ['בעיה', 'תגובה ראשונה', 'תגובה שנייה','תגובה שלישית']
	if type == 'רמז קולי':
		file = filedialog.askopenfile(parent=ROOT,mode='rb',title=type + ' עבור תרחיש מספר ' + str(i), filetypes =[('Audio Files', '*.mp3 *.opus *.ogg *.aac *.flac')])
		fname = file.name
		suff = fname.split('.')[-1]
		shutil.copy(fname, os.path.join(dest_dir, "hint", "hint" + str(i) + '.' + suff))
		files = [suff]
	elif type == 'רמז':
		file = filedialog.askopenfile(parent=ROOT,mode='rb',title=type + ' כתוב עבור תרחיש מספר ' + str(i), filetypes =[('Text File', '*.txt')])
		lines = file.read()
		hint = lines.decode()
		hint = hint.replace('\r\n','<br>')
		hint = hint.replace('\n','<br>')
		files.append(hint)
	else:
		files = []
		for j in range(4):
			if 'תמונה' in type:
				write_to = os.path.join(dest_dir, "img\\")
				filetypes =[('Image Files', '*.png *.jpg *.jpeg *.gif *.webp *.bmp')]
			else:
				write_to = os.path.join(dest_dir, "vid\\")
				filetypes =[('Video Files', '*.mp4 *.webm *.3gp *.ogg')]
				title = type + str_arr[j] + ' עבור תרחיש מספר ' + str(i)
				file = filedialog.askopenfile(parent=ROOT,mode='rb',title=title)
				fname = file.name
			shutil.copy(fname, write_to)
			files.append(fname.split('/')[-1])
	return files

cpit('css')
#cpit('scripts')
cpit('img')
cpit('vid')
cpit('hint')
cpit('done')
res = messagebox.askquestion('שמירת נתונים', '?האם תרצו לשמור נתונים מכל מפגש')
d = os.path.join(dest_dir, "scripts")
if not os.path.exists(d):
	os.makedirs(d)
content = '''
var text = '';
var q=0;
var filename;

function get_participant_num(){
	text = prompt("אנא הכניסו שם/מספר משתתף");
	filename = text + '.csv';
	text += ',' + get_the_date() + '\\r\\n';
}

function next_page(q_or_a){
	answers=[];
	document.getElementById('page_' + q + q_or_a).remove();
	text += getNow() + ',clicked next screen\\r\\n';
	if (q_or_a == 'a') {
		if (q < N){
			q_or_a = 'q';
		}
		else{
			text += getNow() + ',completed\\r\\n';
			console.log(text);
			//console.save(text,filename);
			location.replace('done/Done.html');
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
	text += getNow() + ',' + elem.id + "selected\\r\\n";
	document.getElementById("check" + q).style.display = 'block';
}

function get_the_date(){
	var date = new Date();
	var the_date = date.toLocaleString('en-GB')
	return the_date;
}


(function(console){

	console.save = function(data, filename){

		if(!data) {
			console.error('Console.save: No data')
			return;
		}
 

		if(!filename) filename = 'console.json'

		if(typeof data === "object"){
			data = JSON.stringify(data, undefined, 4)
		}

		var blob = new Blob([data], {type: 'text/json'}),
			e = document.createEvent('MouseEvents'),
			a = document.createElement('a')

		a.download = filename
		a.href = window.URL.createObjectURL(blob)
		a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
		e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
		a.dispatchEvent(e)


	}
})(console)


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

'''

if res == 'yes' :
	content = content.replace('//console.save(text', 'console.save(text')
d = os.path.join(d, 'app.js')
with open(d, 'w',encoding="utf-8") as file:
		file.write(content)

N = simpledialog.askinteger(title="מספר תרחישים", prompt="?כמה תרחישים יש בפעילות")
content = f'''
<!DOCTYPE html>
<html>
	<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width">
	<script src="scripts/app.js"></script>
	<script>const N = {str(N):s};</script>
	<link rel="stylesheet" type="text/css" href="css/powermod.css">
	<title>PowerMod HTML</title>
	</head>
	<body onload="get_participant_num()" onclick="text += getNow() + ',wrong click\\r\\n'">
		<div id="page_0a">
			<svg
			 style="max-height: 98vh;"
			 viewBox="0 0 21.166666 21.166667">
				<path
				 style="fill:none;stroke:#00ff00;stroke-width:1.04387"
				 d="M 0.52202292,6.251575 0.52193499,0.5060963 H 6.2674704 m 8.6317466,5.162e-5 5.745427,-5.162e-5 3.5e-5,5.7454787 m 5.3e-5,8.631767 v 5.745427 h -5.745515 m -8.6317463,8.9e-5 -5.74553571,3.5e-5 3.444e-5,-5.745551" />
				<rect
				 style="fill:none;fill-opacity:1;stroke:#00ff00;stroke-width:1.05833;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1"
				 width="12.633854"
				 height="12.236979"
				 x="4.2664027"
				 y="4.4490047" />
			</svg>
		</div>
		<div id="all_vids">
'''
msg = '''
כעת עלינו לאסוף את כל הקבצים הרלוונטיים
נתחיל בסרטוני הוידאו המציגים את הבעיה עבור כל תרחיש
לפי סדר: סרטון בעיה, סרטון פתרון ראשון, שני ושלישי
'''
vids = []
pics = []
hints = []
messagebox.showinfo(title='סרטוני בעיה', message=msg)
for i in range(N):
	vids.append(file_collector(i+1,'סרטון '))


msg = '''
נמשיך בתמונות מייצגות עבור כל סרטון
לפי סדר: סרטון בעיה, סרטון פתרון ראשון, שני ושלישי
'''
messagebox.showinfo(title='תמונה מייצגת', message=msg)
for i in range(N):
	pics.append(file_collector(i+1,'תמונה מייצגת עבור סרטון '))


msg = '''
עכשיו נבחר את קבצי השמע המוקלטים עם רמז למשתתפים
עבור כל תרחיש
'''
messagebox.showinfo(title='רמזים', message=msg)
for i in range(N):
	hints.append(file_collector(i+1,'רמז קולי'))

msg = '''
ונסיים בבחירת קבצי הטקטס עם רמז למשתתפים עבור כל תרחיש
'''
messagebox.showinfo(title='רמזים', message=msg)
for i in range(N):
	hints.append(file_collector(i+1,'רמז'))

vids_txt=''
for i in range(N):
	vids_txt += f'''
				<div id="Modal_hint{str(i+1):s}" class="hint_modal">
				<div class="modal-content">
					<span class="close">&times;</span>
					<p>{hints[i+N]:s}</p>
				</div>
			</div>
			<div id="Q{str(i+1):s}_video" class="modal">
				<div class="modal-content">
					<video>
						<source src="vid/{vids[i][0]:s}" type="video/mp4">
					</video>
				</div>
			</div>
			<div id="A{str(i+1):s}_1_video" class="modal">
				<div class="modal-content">
					<video>
						<source src="vid/{vids[i][1]:s}" type="video/mp4">
					</video>
				<svg viewBox="0 0 7.9374998 7.9375">
						<path
							 style="fill:#0000ff"
							 id="path1"
							 d="M 3.974425,5.4320933 0.36552733,3.4615504 -3.2433701,1.4910075 0.267619,-0.64911804 3.7786079,-2.7892435 3.8765164,1.3214251 Z"
							 transform="matrix(0.84701854,-0.53429998,0.46278965,0.97789998,2.0571718,4.7465113)" />
				</svg>
				</div>
			</div>
			<div id="A{str(i+1):s}_2_video" class="modal">
				<div class="modal-content">
					<video>
						<source src="vid/{vids[i][2]:s}" type="video/mp4">
					</video>
				<svg viewBox="0 0 7.9374998 7.9375">
						<circle
							 style="fill:#00ff00"
							 id="path1"
							 cx="3.96875"
							 cy="3.96875"
							 r="3.96875" />
				</svg>
				</div>
			</div>
			<div id="A{str(i+1):s}_3_video" class="modal">
				<div class="modal-content">
					<video>
						<source src="vid/{vids[i][3]:s}" type="video/mp4">
					</video>
				<svg viewBox="0 0 7.9374998 7.9375">
						<rect
							 style="fill:#aa4acf;fill-opacity:1"
							 id="rect1"
							 width="7.9375"
							 height="7.9375"
							 x="-2.220446e-16"
							 y="0" />
				</svg>
				</div>
			</div>
	'''


content += vids_txt + '<div>'

pics_txt=''


for i in range(N):
	print (i)
	pics_txt += f'''
		<div id="page_{str(i+1):s}q" class="q_page" style="display:none">
		<div class="overlay">
			<div class="icons">
				<svg viewBox="0 0 7.9374998 7.9375">
					<path
						 style="fill:#0000ff"
						 d="M 3.974425,5.4320933 0.36552733,3.4615504 -3.2433701,1.4910075 0.267619,-0.64911804 3.7786079,-2.7892435 3.8765164,1.3214251 Z"
						 transform="matrix(0.84701854,-0.53429998,0.46278965,0.97789998,2.0571718,4.7465113)" />
				</svg>
				<svg viewBox="0 0 7.9374998 7.9375">
					<circle
						 style="fill:#00ff00"
						 cx="3.96875"
						 cy="3.96875"
						 r="3.96875" />
				</svg>
				<svg viewBox="0 0 7.9374998 7.9375">
					<rect
						 style="fill:#aa4acf;fill-opacity:1"
						 width="7.9375"
						 height="7.9375"
						 x="-2.220446e-16"
						 y="0" />
				</svg>
			</div>
		</div>
		<div class="container">
			<div class="up">
				<div></div>
				<img src="img/{pics[i][0]:s}" id="Q{str(i+1):s}q" class="Q_img" />
				<div id="next_q_1"></div>
			</div>
			<div class="ans">
				<div>
					<img src="img/{pics[i][1]:s}" id="A{str(i+1):s}_1q" class="Q_img" />
				</div>
				<div>
					<img src="img/{pics[i][2]:s}" id="A{str(i+1):s}_2q" class="Q_img"/>
				</div>
				<div>
					<img src="img/{pics[i][3]:s}" id="A{str(i+1):s}_3q" class="Q_img"/>
				</div>
			</div>
		</div>
		</div>
		<div id="page_{str(i+1):s}a" style="display:none" class="a_page">
		<div class="overlay">
			<div class="icons">
			<div>
				<svg viewBox="0 0 7.9374998 7.9375">
					<path
						 style="fill:#0000ff"
						 d="M 3.974425,5.4320933 0.36552733,3.4615504 -3.2433701,1.4910075 0.267619,-0.64911804 3.7786079,-2.7892435 3.8765164,1.3214251 Z"
						 transform="matrix(0.84701854,-0.53429998,0.46278965,0.97789998,2.0571718,4.7465113)" />
				</svg>
				<svg
					id="A{str(i+1):s}_1a"
					class="movie_svg Q_img"
					viewBox="0 0 7.9374998 7.9375" >
					<defs>
						<marker
							style="overflow:visible"
							id="Triangle"
							refX="0"
							refY="0"
							orient="auto-start-reverse"
							markerWidth="0.7"
							markerHeight="0.7"
							viewBox="0 0 1 1"
							preserveAspectRatio="xMidYMid">
						<path
							transform="scale(0.5)"
							style="fill:context-stroke;fill-rule:evenodd;stroke:context-stroke;stroke-width:1pt"
							d="M 5.77,0 -2.88,5 V -5 Z" />
						</marker>
					</defs>
					<rect
						style="fill:#813ab8;fill-opacity:1;stroke:#ffffff;stroke-width:0.126993;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
						width="6.1746221"
						height="3.7379994"
						x="0.17065275"
						y="1.9866134" />
					<path
							style="fill:#813ab8;fill-opacity:1;stroke:#ffffff;stroke-width:0.0877679;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
							d="m 7.8305192,2.6029177 -1.3970774,0.556089 v 0.696878 0.6963345 l 1.3970774,0.556089 V 3.8558847 Z" />
					<path
							style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0998443;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
							d="M 3.9233267,3.8556131 3.3672417,4.1766687 2.8111572,4.4977242 V 3.8556131 3.2135018 l 0.5560845,0.3210553 z" />
					<path
							style="fill:none;stroke:#ffffff;stroke-width:0.194209;stroke-linejoin:round;stroke-dasharray:none;marker-start:url(#Triangle)"
							d="m 3.931821,2.8142219 c 0.3788666,0.2198439 0.6322004,0.6194669 0.6322004,1.0759834 0,0.6935727 -0.584742,1.2558247 -1.3060577,1.2558247 -0.7213157,0 -1.3060576,-0.562252 -1.3060576,-1.2558247 0,-0.5957297 0.4313983,-1.0945761 1.010199,-1.2234662 0.095063,-0.021168 0.1941017,-0.03236 0.2958586,-0.03236" />
				</svg>
				</div>
				<div>
				<svg viewBox="0 0 7.9374998 7.9375">
					<circle
						 style="fill:#00ff00"
						 cx="3.96875"
						 cy="3.96875"
						 r="3.96875" />
				</svg>
				<svg
					id="A{str(i+1):s}_2a"
					class="movie_svg Q_img"
					viewBox="0 0 7.9374998 7.9375" >
					<defs>
						<marker
							style="overflow:visible"
							id="Triangle"
							refX="0"
							refY="0"
							orient="auto-start-reverse"
							markerWidth="0.7"
							markerHeight="0.7"
							viewBox="0 0 1 1"
							preserveAspectRatio="xMidYMid">
						<path
							transform="scale(0.5)"
							style="fill:context-stroke;fill-rule:evenodd;stroke:context-stroke;stroke-width:1pt"
							d="M 5.77,0 -2.88,5 V -5 Z" />
						</marker>
					</defs>
					<rect
						style="fill:#813ab8;fill-opacity:1;stroke:#ffffff;stroke-width:0.126993;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
						width="6.1746221"
						height="3.7379994"
						x="0.17065275"
						y="1.9866134" />
					<path
							style="fill:#813ab8;fill-opacity:1;stroke:#ffffff;stroke-width:0.0877679;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
							d="m 7.8305192,2.6029177 -1.3970774,0.556089 v 0.696878 0.6963345 l 1.3970774,0.556089 V 3.8558847 Z" />
					<path
							style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0998443;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
							d="M 3.9233267,3.8556131 3.3672417,4.1766687 2.8111572,4.4977242 V 3.8556131 3.2135018 l 0.5560845,0.3210553 z" />
					<path
							style="fill:none;stroke:#ffffff;stroke-width:0.194209;stroke-linejoin:round;stroke-dasharray:none;marker-start:url(#Triangle)"
							d="m 3.931821,2.8142219 c 0.3788666,0.2198439 0.6322004,0.6194669 0.6322004,1.0759834 0,0.6935727 -0.584742,1.2558247 -1.3060577,1.2558247 -0.7213157,0 -1.3060576,-0.562252 -1.3060576,-1.2558247 0,-0.5957297 0.4313983,-1.0945761 1.010199,-1.2234662 0.095063,-0.021168 0.1941017,-0.03236 0.2958586,-0.03236" />
				</svg>
				</div>
				<div>
				<svg viewBox="0 0 7.9374998 7.9375">
					<rect
						 style="fill:#aa4acf;fill-opacity:1"
						 width="7.9375"
						 height="7.9375"
						 x="-2.220446e-16"
						 y="0" />
				</svg>
				<svg
					id="A{str(i+1):s}_3a" 
					class="movie_svg Q_img"
					viewBox="0 0 7.9374998 7.9375" >
					<defs>
						<marker
							style="overflow:visible"
							id="Triangle"
							refX="0"
							refY="0"
							orient="auto-start-reverse"
							markerWidth="0.7"
							markerHeight="0.7"
							viewBox="0 0 1 1"
							preserveAspectRatio="xMidYMid">
						<path
							transform="scale(0.5)"
							style="fill:context-stroke;fill-rule:evenodd;stroke:context-stroke;stroke-width:1pt"
							d="M 5.77,0 -2.88,5 V -5 Z" />
						</marker>
					</defs>
					<rect
						style="fill:#813ab8;fill-opacity:1;stroke:#ffffff;stroke-width:0.126993;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
						width="6.1746221"
						height="3.7379994"
						x="0.17065275"
						y="1.9866134" />
					<path
							style="fill:#813ab8;fill-opacity:1;stroke:#ffffff;stroke-width:0.0877679;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
							d="m 7.8305192,2.6029177 -1.3970774,0.556089 v 0.696878 0.6963345 l 1.3970774,0.556089 V 3.8558847 Z" />
					<path
							style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0998443;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:1"
							d="M 3.9233267,3.8556131 3.3672417,4.1766687 2.8111572,4.4977242 V 3.8556131 3.2135018 l 0.5560845,0.3210553 z" />
					<path
							style="fill:none;stroke:#ffffff;stroke-width:0.194209;stroke-linejoin:round;stroke-dasharray:none;marker-start:url(#Triangle)"
							d="m 3.931821,2.8142219 c 0.3788666,0.2198439 0.6322004,0.6194669 0.6322004,1.0759834 0,0.6935727 -0.584742,1.2558247 -1.3060577,1.2558247 -0.7213157,0 -1.3060576,-0.562252 -1.3060576,-1.2558247 0,-0.5957297 0.4313983,-1.0945761 1.010199,-1.2234662 0.095063,-0.021168 0.1941017,-0.03236 0.2958586,-0.03236" />
				</svg>
				</div>
			</div>
		</div>
		<div class="container">
			<div class="up">
				<img src="img/hint.png" id="hint{str(i+1):s}" filetype=".{hints[i]:s}" class="show_hint"/>
				<img src="img/{pics[i][0]:s}" id="Q{str(i+1):s}a" class="Q_img"/>
				<svg
					viewBox="0 0 21.166666 21.166667" style="height: 33vh;display:none" class="next_page" id="check{str(i+1):s}">
					<path
						style="font-size:22.5778px;font-family:'DejaVu Serif';-inkscape-font-specification:'DejaVu Serif, Normal';fill:#ffffff;stroke:#ffffff;stroke-width:1.124;stroke-linejoin:round"
						d="M 17.988825,19.117525 H 2.3875644 V 3.5162648 H 17.988825 Z m -0.72249,-0.72249 V 4.2387544 H 3.1100541 V 18.395035 Z M 5.0065893,13.179564 q 0,-0.383823 0.5644451,-0.699912 0.5870228,-0.31609 0.9256898,-0.31609 0.2483558,0 0.564445,0.880535 0.3160892,0.857956 0.4967116,0.857956 0.112889,0 0.3838226,-0.451556 1.2417791,-2.099735 2.6190246,-4.0414262 1.377246,-1.9642687 2.235203,-2.7319139 0.790223,-0.7224896 2.438402,-0.7224896 v 0.2483558 q -1.919113,2.032002 -3.476981,4.1994709 -1.535291,2.144891 -2.2352025,3.409248 -0.677334,1.241779 -1.3546681,2.05458 -0.6547562,0.812801 -1.2643568,0.812801 -0.4967116,0 -0.903112,-0.51929 Q 5.61619,15.640544 5.4129897,14.96321 5.2097895,14.285876 5.0969005,13.789164 q -0.090311,-0.496711 -0.090311,-0.6096 z"
						aria-label="checkmark" />
				</svg>
			</div>
			<div class="ans">
				<div>
					<img src="img/{pics[i][1]:s}" id="image_A{str(i+1):s}_1" class="choose_answer"/>
				</div>
				<div>
					<img src="img/{pics[i][2]:s}" id="image_A{str(i+1):s}_2" class="choose_answer"/>
				</div>
				<div>
					<img src="img/{pics[i][3]:s}" id="image_A{str(i+1):s}_3" class="choose_answer"/>
				</div>
			</div>
		</div>
		</div>
	'''


content += vids_txt
content += pics_txt
content +='''
		<script>
			var answers=[];
			var vid;
			function show_modal(elem){
				var id = elem.id.slice(0, -1) + "_video";
				text += getNow() + ',' + id + '\\r\\n';
				modal = document.getElementById(id);
				if (!(answers.includes(id))){
					answers.push(id);
				}
				modal.style.display = "block";
				elem.style.borderColor = "#803aff";
				vid = modal.getElementsByTagName('video')[0];
				vid.play();
				vid.addEventListener('ended',myHandler,false);
				function myHandler(e) {
					modal.style.display = "none";
					text += getNow() + ',' + id + ' ended\\r\\n';
					if ((elem.id.slice(-1)) == 'q' && (answers.length >= 4)){
						next_page('q');
					}
				}
				window.onclick = function(event) {
					if (event.target == modal) {
						modal.style.display = "none";
						vid.pause();
						text += getNow() + ',' + id + ' paused\\r\\n';
					}
				}
			}
			var images = document.getElementsByClassName('Q_img'); 
			for(var i = 0; i < images.length; i++) {
				images[i].addEventListener("click",function (e) {
					e.stopPropagation();
					show_modal(this);
				});
			}
			images = document.getElementsByClassName('choose_answer'); 
			for(var i = 0; i < images.length; i++) {
				images[i].addEventListener("click",function (e) {
					e.stopPropagation();
					choose_answer(this);
				});
			}
			
			images = document.getElementsByClassName('next_page'); 
			for(var i = 0; i < images.length; i++) {
				images[i].addEventListener("click",function (e) {
					e.stopPropagation();
					next_page('a');
				});
			}
			
			var hinties = document.getElementsByClassName('show_hint'); 
			for(var i = 0; i < hinties.length; i++) {
				hinties[i].addEventListener("click",function (e) {
					e.stopPropagation();
					show_hint(this);
				});
			}
			var spans = document.getElementsByTagName('span'); 
				for(var i = 0; i < spans.length; i++) {
				spans[i].addEventListener("click",function (e) {
					e.stopPropagation();
					modal.style.display = "none";
					vid.pause();
					text += getNow() + ',paused by clicking X\\r\\n';
				});
				}
			var modal;
			function show_hint(elem){
				var id = elem.id;
				text += getNow() + ',' + id + '\\r\\n';
				modal = document.getElementById("Modal_" + id);
				var span = modal.getElementsByClassName("close")[0];
				modal.style.display = "block";
				vid = new Audio("hint/" + id + elem.getAttribute("filetype"));
				vid.play();
				vid.addEventListener('ended',myHandler,false);
				function myHandler(e) {
					modal.style.display = "none";
					text += getNow() + ',' + id + ' ended\\r\\n';
				}
				window.onclick = function(event) {
					if (event.target == modal) {
						modal.style.display = "none";
						vid.pause();
						text += getNow() + ',' + id + ' paused\\r\\n';
					}
				}
			}
			document.getElementById('page_0a').addEventListener("click",function (e) {
				e.stopPropagation();
				document.body.requestFullscreen();
				next_page('a');
			});
		</script>
	</body>
</html>
'''

with open(os.path.join(dest_dir, "PowerMod.html"), "w", encoding = "utf-8") as f:
	f.write(content)



msg = '''
נותר לנו לארוז את הכל לקובץ תמונת דיסק
אנא בחרו את מיקום הקובץ
'''
messagebox.showinfo(title='מיקום סופי', message=msg)
output = filedialog.askdirectory()
output = os.path.join(output.replace('/','\\'),'PowerMod.iso')
os.popen('"' + os.path.join(cwd, 'tools', 'mkisofs.exe"') + ' -udf -o "' + output + '" "' + dest_dir + '"')
