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
##  Python HTTP API Activity
A resource based python HTTP client for RESTful APIs that use JSON 
### Usage
**Example**
```bash
$ cd api_app
api_app$ python
>>> from custom_api import Resource
>>> my_api = Resource('127.0.0.1', '/api/v1/:endpoint/:id', 8080, {'Content-Type':'application/json', 'charset':'utf-8'})
>>> response = my_api.post({'refreshToken':'8ds8f6e8y'}, {'endpoint':'auth/http'})
>>> print response
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9FF3V-2QNQarwuef1oKjFkWYEkv1nrAQ=="}
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
