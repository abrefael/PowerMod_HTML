#!/usr/bin/python

import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import shutil
import webbrowser
import io


def buildTree(parent_dir,chld_dir):
	try:
		path = os.path.join(parent_dir, chld_dir)
		os.mkdir(path)
	except OSError as error:
		pass

cwd = os.path.dirname(os.path.realpath(__file__))

class MyHandler(SimpleHTTPRequestHandler):
	def do_POST(self):
<<<<<<< Updated upstream
		def cpit(src_lst,dst_lst):
			src = os.path.join(*src_lst)
			dst = os.path.join(*dst_lst)
			try:
				shutil.copytree(src, dst)
			except NotADirectoryError:
				shutil.copy(src, dst)
			except Exception as e:
				print(f"Something went wrong: {e}")
=======
		import sys
		from pathlib import Path
		def cpit(src: str | Path, dst: str | Path) -> None:
			src_path = Path(src).expanduser()
			dst_path = Path(dst).expanduser()
			if not src_path.exists():
				raise FileNotFoundError(f"Source does not exist: {src_path}")
			if src_path.is_file():
				shutil.copy2(src_path, dst_path)
				print(f"{src_path} copied to {dst_path}")
				return
			try:
				shutil.copytree(
					src_path,
					dst_path,
					dirs_exist_ok=True,
					copy_function=shutil.copy  # NOT copy2
				)
				print(f"{src_path} copied to {dst_path}")
			except PermissionError:
				cmd = f'robocopy "{src_path}" "{dst_path}" /E /COPY:DAT /R:1 /W:1'
				code = os.system(cmd)
				if code >= 8:
					raise PermissionError(f"robocopy failed with exit code {code}")
>>>>>>> Stashed changes
		def rep_all(orig,replace_dict):
			for key in replace_dict.keys():
				orig = orig.replace(key,replace_dict[key])
			return orig
		cwd = os.path.dirname(os.path.realpath(__file__))
<<<<<<< Updated upstream
		buildTree(cwd,'Output')
		res = os.path.join(cwd,'Put_Media_Files_in_Here')
		cwd = os.path.join(cwd,'Output')
=======
		buildTree(cwd,'Play')
		res = os.path.join(cwd,'Put_Media_Files_in_Here')
		cwd = os.path.join(cwd,'Play')
>>>>>>> Stashed changes
		buildTree(cwd,'css')
		buildTree(cwd,'img')
		buildTree(cwd,'vid')
		buildTree(cwd,'hint')
		buildTree(cwd,'done')
		buildTree(cwd,'scripts')
		if self.path == '/data':
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read(content_length)
			data = json.loads(post_data)
			print("Received JSON:", data)
			src = os.path.join(os.path.dirname(os.path.realpath(__file__)),'.templates')
			n_or_m = data['m_or_n']
<<<<<<< Updated upstream
			cpit([src,n_or_m + '.css'],[cwd,'css','powermod.css'])
			cpit([src,'Done.html'],[cwd,'done','Done.html'])
			cpit([src,'hint.png'],[cwd,'img','hint.png'])
			cpit([src,'video-js-8.23.3'],[cwd,'scripts','video-js-8.23.3'])
=======
			cpit(os.path.join(src,n_or_m + '.css'),os.path.join(cwd,'css','powermod.css'))
			cpit(os.path.join(src,'Done.html'),os.path.join(cwd,'done','Done.html'))
			cpit(os.path.join(src,'hint.png'),os.path.join(cwd,'img','hint.png'))
			cpit(os.path.join(src,'video-js-8.23.3'),os.path.join(cwd,'scripts','video-js-8.23.3'))
>>>>>>> Stashed changes
			app_js = io.open(os.path.join(src,'app.js'), mode="r",encoding="utf-8").read()
			if data['keep_data'] == 'yes' :
				app_js = app_js.replace('//', '')
				app_js = app_js.replace('{br}', '\\r\\n')
			with open(os.path.join(cwd,'scripts','app.js'), 'w',encoding="utf-8") as file:
				file.write(app_js)
			pm_html = open(os.path.join(src,'pm_start'), "r").read()
			N = int(data['N'])
			for key in data.keys():
				if 'img' in key:
					cpit([res,data[key]],[cwd,'img',data[key]])
				elif 'vid' in key:
					cpit([res,data[key]],[cwd,'vid',data[key]])
				elif 'aud' in key:
					suff = data[key].split('.')[-1]
					cpit([res,data[key]],[cwd,'hint',key + '.' + suff])
					data[key] = suff
			pm_html = pm_html.replace('{(N)}',str(N))
			for i in range(N):
				pm_html += open(os.path.join(src,n_or_m + '_pt1'), "r").read()
				pm_html = rep_all(pm_html,{'{str(i+1)}':str(i+1),
					'{vids[i][0]}':data['vid_' + str(i+1) + '_0'],
					'{vids[i][1]}':data['vid_' + str(i+1) + '_1'],
					'{vids[i][2]}':data['vid_' + str(i+1) + '_2']
				})
				if '{vids[i][3]}' in pm_html:
					pm_html = rep_all(pm_html,{'{vids[i][3]}':data['vid_' + str(i+1) + '_3'],
						'{hints[i]}':data['text_hint_' + str(i+1)]
					})
			for i in range(N):
				pm_html += open(os.path.join(src,n_or_m + '_pt2'), "r").read()
				pm_html = rep_all(pm_html,{'{str(i+1)}':str(i+1),
					'{pics[i][0]}':data['img_' + str(i+1) + '_0'],
					'{pics[i][1]}':data['img_' + str(i+1) + '_1'],
					'{pics[i][2]}':data['img_' + str(i+1) + '_2']
				})
				if '{pics[i][3]}' in pm_html:
					pm_html = rep_all(pm_html,{'{pics[i][3]}':data['img_' + str(i+1) + '_3'],
						'{hints[i]}':'aud_' + str(i+1) + '_0.' + data['aud_' + str(i+1) + '_0']
					})
			pm_html += open(os.path.join(src,n_or_m + '_pt3'), "r").read()
			with open(os.path.join(cwd, "PowerMod.html"), "w", encoding = "utf-8") as f:
				f.write(pm_html.replace('{br}', '\\r\\n'))
			self.send_response(200)
			self.send_header('Content-type', 'text/plain')
			self.end_headers()
			self.wfile.write(b"JSON received successfully")
			exit()
		else:
			self.send_error(404, "File not found")



if __name__ == '__main__':
	try:
		os.remove(os.path.join(cwd,'Put_Media_Files_in_Here','.deme'))
	except OSError:
		pass
	server_address = ('', 8889)
	httpd = HTTPServer(server_address, MyHandler)
	webbrowser.open('http://localhost:8889/.HTML')
	print("Serving on port 8889...")
	httpd.serve_forever()

