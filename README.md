#   Day 2 of Andela Bootcamp XIV
Clone the repo using the link above
##  AndeLabs
### Word Count
Run the tests defined on AndeLabs. Test for word_count is saved as `test_word.py`
```bash
$ cd word_count
word_count$ pytest
no test dir found testing here: ./
===========================  test_word.py  ===========================
..........
*******************************************************************************
Ran 10 test cases in 0.00s (0.00s CPU)
All 1 modules OK
```
### Max and Min Number
Run the tests defined on AndeLabs. Test for word_count is saved as `test_max_min.py`
```bash
$ cd max_min
max_min$ pytest
no test dir found testing here: ./
=========================  test_max_min.py  ==========================
.....
*******************************************************************************
Ran 5 test cases in 0.00s (0.00s CPU)
All 1 modules OK
```
##  Python HTTP API Activity - `my_app.py`
Accepts two arguments from the commandline
```bash
$cd api_app
api_app$ python my_app.py 'twende.techstart.co.ke' '/api/v1/:endpoint/:id'
A simple program to refresh a token at the public API found here -twende.techstart.co.ke/api/v1/:endpoint/:id
Add it to the header and use it to fetch a list of users
Getting new token ...
Adding new token to Auth header ...
New Token Data- {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXV...', 'type': 'Bearer'}
Fetching User List ...


{"code":"001","message":"Unauthorized - Invalid Token"}

 Thank you ...
```
Uses a custom resource based python HTTP client for RESTful APIs that use JSON 
### Usage
**Example**
```bash
$ cd api_app
api_app$ python
>>> from custom_api import Resource
>>> my_api = Resource('127.0.0.1', '/api/v1/:endpoint/:id', 8080, {'Content-Type':'application/json', 'charset':'utf-8'})
>>> response = my_api.post({'refreshToken':'8ds8f6e8y'}, {'endpoint':'auth/http'})
>>> print response
{'status': '200 HTTP/1.1', 'headers': [('content-length', '325'), ('x-powered-by', 'Express'), ('connection', 'keep-alive'), ('etag', 'W/"145-IwBmyNr5CxYlU9bhtX2UaQ"'), ('date', 'Wed, 18 Jan 2017 12:12:31 GMT'), ('access-control-allow-origin', '*'), ('content-type', 'application/json; charset=utf-8')], 'data': '{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ97l53MiOiJodHRwOi8vdHdlbmRlLnRlY=="}'}
```
### Instanciation
`Resource( host, resource_URI[, port[, default_headers]] )`

**host** - a string of the domain name or IP address

**resource_URI** - a string of the resource that contains abstract parts of the url replaced dynamically by corresponding values in the parameters sent to member functions

**port** - (optional) a number representing the port. Defaults to 80

**default_headers** - (optional) a dictionary containing key-pair values of HTTP header information. Defaults to None

### Instance Methods
`action(action, body[, params[, headers]])`

**action** - a string respresenting HTTP action eg. PUT, DELETE

**body** - a dictionary containing the HTTP body in key-pair values. Defaults to None

**params** - (optional) a dictionary key-pair values to be included dynamically in the URI defined during instanciation. Defaults to None

**headers** - (optional) a dictionary containing HTTP header information. If this is set, all default headers except Authorization are overwriten. Defaults to None

`get([params[, headers]])`

**params** - (optional) a dictionary key-pair values to be included dynamically in the URI defined during instanciation. Defaults to None

**headers** - (optional) a dictionary containing HTTP header information. If this is set, all default headers except Authorization are overwriten. Defaults to None

`post(body[, params[, headers]])`

**body** - a dictionary containing the HTTP body in key-pair values

**params** - (optional) a dictionary key-pair values to be included dynamically in the URI defined during instanciation. Defaults to None

**headers** - (optional) a dictionary containing HTTP header information. If this is set, all default headers except Authorization are overwriten. Defaults to None

`useAuth(auth_type, auth_details)`

**auth_type** - a string with the authorization type eg. Bearer

**auth_details** - a string with the authorization details eg a JSON web token

*useAuth() sets a default authorization header to be sent with all following requests, so use it carefully
