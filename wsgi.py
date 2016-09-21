#!/usr/bin/env python

from cgi import escape

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	uri = escape(uri)
	response_body = "isina : "+uri

	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [response_body]

