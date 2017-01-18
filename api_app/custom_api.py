import httplib, json

class Resource(object):
	
	def __init__(self, host, resourceURI, port = 80, defaultHeaders = None):
		self.host = host
		self.port = port
		self.URI = resourceURI
		self.defaultHeaders = defaultHeaders
	
	def action(self, action, body = None, params = None, headers = None):
		if headers is None:
			headers = self.defaultHeaders
		if self.useAuth is True:
			headers['Authorization'] = self.auth['type'] + ': ' + self.auth['token']
		url = self.URI
		if params is not None:
			for k, v in params.items():
				url.replace(':'+k, v)
		url = url.split(':')[0]
		conn = httplib.HTTPConnection(self.host, self.port, False, 300)
		conn.request(action, url, json.dumps(body), headers)
		resp = conn.getresponse()
		resp = {'status':str(resp.status)+' HTTP/'+str(resp.version)[0]+'.'+str(resp.version)[0],'headers':resp.getheaders(),'data':str(resp.read())}
		conn.close()
		return resp

	def get(self, params = None, headers = None):
		if headers is None:
			headers = self.defaultHeaders
		if self.useAuth is True:
			headers['Authorization'] = self.auth['type'] + ': ' + self.auth['token']
		url = self.URI
		if params is not None:
			for k, v in params.items():
				url = url.replace(str(':'+k), str(v))
		url = url.split(':')[0]
		conn = httplib.HTTPConnection(self.host, self.port, False, 300)
		conn.request('GET', url, None, headers)
		resp = conn.getresponse()
		resp = {'status':str(resp.status)+' HTTP/'+str(resp.version)[0]+'.'+str(resp.version)[0],'headers':resp.getheaders(),'data':str(resp.read())}
		conn.close()
		return resp

	def post(self, body, params = None, headers = None):
		if headers is None:
			headers = self.defaultHeaders
		if self.useAuth is True:
			headers['Authorization'] = self.auth['type'] + ': ' + self.auth['token']
		url = self.URI
		if params is not None:
			for k, v in params.items():
				url = url.replace(str(':'+k), str(v))
		url = url.split(':')[0]
		conn = httplib.HTTPConnection(self.host, self.port, False, 300)
		conn.request('POST', url, json.dumps(body), headers)
		resp = conn.getresponse()
		resp = {'status':str(resp.status)+' HTTP/'+str(resp.version)[0]+'.'+str(resp.version)[0],'headers':resp.getheaders(),'data':str(resp.read())}
		conn.close()
		return resp

	def useAuth(self, authType, authToken):
		self.auth = {}
		self.auth['type'] = authType
		self.auth['token'] = authToken
		self.useAuth = True
		return self.auth
