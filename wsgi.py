def application(environ, start_response):
	response_body = [
		'%s: %s' % (key, value) for key, value in sorted(environ.items())
	]
	response_body = '\n'.join(response_body)

	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [response_body]

