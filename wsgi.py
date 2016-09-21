#!/usr/bin/env python

import gitar
from cgi import escape
import config

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	uri = escape(uri)
	gr = gitar.Gitar()

	if uri == config.uri1:
		respon=gr.gitpull(config.dir1,config.host1,config.username1,config.password2)		
	elif uri == config.uri2:
		respon=gr.gitpull(confid.dir2,config.host2,config.username1,config.password2)
	else:
		respon="oke"


	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

