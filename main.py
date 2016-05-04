def app(environ, start_response):
	start_response('200-OK',[('content-type','text/html')])
	return  ['Hello Python Word!']

if __name__ == "__main__":
	from paste import httpserver
	httpserver.server(app,host='127.0.0.1',port='8080')