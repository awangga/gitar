#!/usr/bin/env python

from cgi import parse_qs, escape

def application(environ, start_response):
	id = environ['PATH_INFO']
	#id = d.get('id', [''])[0]	

	id = escape(id)
	response_body = "isina : "+id

	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [response_body]

