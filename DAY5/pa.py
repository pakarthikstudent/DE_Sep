import http.server

from prometheus_client import start_http_server

class myclass(http.server.BaseHTTPRequestHandler):
	def f1(self):
		self.send_reponse(200)
		self.end_headers()
		self.wfile(b'Hello world')


if __name__ == '__main__':
     start_http_server(8000)
     server = http.server.HTTPServer(('localhost',8001),myclass)
     server.serve_forever()