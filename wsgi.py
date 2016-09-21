#!/usr/bin/env python

from cgi import parse_qs, escape

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	id = d.get('id', [''])[0]	

	response_body = "isina : "+id

	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [response_body]

