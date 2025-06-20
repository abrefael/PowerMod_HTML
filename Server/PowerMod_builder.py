#!/usr/bin/python

import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import shutil
import platform
import webbrowser



def buildTree(parent_dir,chld_dir):
	try:
		path = os.path.join(parent_dir, chld_dir)
		os.mkdir(path)
	except OSError as error:
		pass

cwd = os.path.dirname(os.path.realpath(__file__))

class MyHandler(SimpleHTTPRequestHandler):
	def do_POST(self):
		def cpit(src,dst):
			try:
				shutil.copy(src, dst)
			except OSError as error:
				pass
		cwd = os.path.dirname(os.path.realpath(__file__))
		buildTree(cwd,'Output')
		res = os.path.join(cwd,'resources')
		cwd = os.path.join(cwd,'Output')
		buildTree(cwd,'css')
		buildTree(cwd,'img')
		buildTree(cwd,'vid')
		buildTree(cwd,'hint')
		buildTree(cwd,'scripts')
		if self.path == '/data':
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read(content_length)
			data = json.loads(post_data)
			src = os.path.join(os.path.dirname(os.path.realpath(__file__)),'templates')
			n_or_m = data['m_or_n']
			cpit(os.path.join(src,n_or_m + '.css'),os.path.join(cwd,'css','powermod.css'))
			cpit(os.path.join(src,'Done.html'),os.path.join(cwd,'Done.html'))
			cpit(os.path.join(src,'hint.png'),os.path.join(cwd,'img','hint.png'))
			app_js = open(os.path.join(src,'app.js'), "r").read()
			if data['keep_data'] == 'yes' :
				app_js = app_js.replace('//console.save(text', 'console.save(text')
			with open(os.path.join(cwd,'scripts','app.js'), 'w',encoding="utf-8") as file:
				file.write(app_js)
			pm_html = open(os.path.join(src,'pm_start'), "r").read()
			N = data['N']
			pm_html = pm_html.replace('{(N)}',str(N))
			for i in range(N):
				pm_html += open(os.path.join(src,n_or_m + '_pt1'), "r").read()
				pm_html = pm_html.replace('{str(i+1)}', str(i+1))
				pm_html = pm_html.replace('{vids[i][0]}', data['vid_' + str(i+1) + '_0'])
				pm_html = pm_html.replace('{vids[i][1]}', data['vid_' + str(i+1) + '_1'])
				pm_html = pm_html.replace('{vids[i][2]}', data['vid_' + str(i+1) + '_2'])
				if '{vids[i][3]}' in pm_html:
					pm_html = pm_html.replace('{vids[i][3]}', data['vid_' + str(i+1) + '_3'])
					pm_html = pm_html.replace('{hints[i]}', data['text_hint_' + str(i+1)])
			for i in range(N):
				pm_html += open(os.path.join(src,n_or_m + '_pt2'), "r").read()
				pm_html = pm_html.replace('{str(i+1)}', str(i+1))
				pm_html = pm_html.replace('{pics[i][0]}', data['img_' + str(i+1) + '_0'])
				pm_html = pm_html.replace('{pics[i][1]}', data['img_' + str(i+1) + '_1'])
				pm_html = pm_html.replace('{pics[i][2]}', data['img_' + str(i+1) + '_2'])
				if '{pics[i][3]}' in pm_html:
					pm_html = pm_html.replace('{pics[i][3]}', data['img_' + str(i+1) + '_3'])
					pm_html = pm_html.replace('hint{str(i+1)}','aud_' + str(i+1) + '_0')
			pm_html += open(os.path.join(src,n_or_m + '_pt3'), "r").read()
			for key in data.keys():
				if 'img' in key:
					cpit(os.path.join(res,data[key]),os.path.join(cwd,'img',data[key]))
				elif 'vid' in key:
					cpit(os.path.join(res,data[key]),os.path.join(cwd,'vid',data[key]))
				elif 'aud' in key:
					cpit(os.path.join(res,data[key]),os.path.join(cwd,'hint',key))
			with open(os.path.join(cwd, "PowerMod.html"), "w", encoding = "utf-8") as f:
				f.write(pm_html)
			print("Received JSON:", data)
			self.send_response(200)
			self.send_header('Content-type', 'text/plain')
			self.end_headers()
			self.wfile.write(b"JSON received successfully")
			exit()
		else:
			self.send_error(404, "File not found")



if __name__ == '__main__':
	buildTree(cwd,'resources')
	server_address = ('', 8889)
	httpd = HTTPServer(server_address, MyHandler)
	webbrowser.open('http://localhost:8889')
	print("Serving on port 8889...")
	httpd.serve_forever()

