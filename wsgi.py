#!/usr/bin/env python

from cgi import escape
import config
import subprocess

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	uri = escape(uri)
	gr = gitar.Gitar()

	if uri == config.uri1:
		pid = subprocess.Popen(["nohup", "python", "1pool.py"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).pid
		respon=str(pid)
	elif uri == config.uri2:
		pid = subprocess.Popen(["nohup", "python", "2pool.py"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).pid
		respon=str(pid)
	else:
		respon="oke"


	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

