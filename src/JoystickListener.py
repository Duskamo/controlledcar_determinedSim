
import threading
import time
from http.server import *
import socketserver
import json

class JoystickListener(threading.Thread):
	def __init__(self,name,inputQueue):
		super(JoystickListener, self).__init__()
		self.name = name
		self.inputQueue = inputQueue

		self.PORT = 5001
		JoystickHandler.inputQueue = self.inputQueue
		self.httpd = socketserver.TCPServer(("localhost", self.PORT), JoystickHandler)

	def run(self):
		print("serving at port", self.PORT)
		self.httpd.serve_forever()


class JoystickHandler(BaseHTTPRequestHandler):
	inputQueue = None
	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)

		bodyDict = json.loads(body)
		print(bodyDict)
		self.inputQueue.put(bodyDict)

		self.send_response(200)
		self.end_headers()
