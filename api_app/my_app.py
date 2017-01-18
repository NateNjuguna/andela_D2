from custom_api import Resource
import sys
my_api = Resource(sys.argv[1], sys.argv[2], sys.argv[3], {'Content-Type':'application/json', 'charset':'utf-8'})

print 'A simple program to refresh a token at the public API found here -' + str(sys.argv[1]) + str(sys.argv[2])
print 'Add it to the header and use it to fetch a list of users'
print 'Getting new token ...'
response = my_api.post({'refreshToken':'RETARTS','agent':'Bauer'}, {'endpoint':'auth/http','id':0})
print 'Adding new token to Auth header ...'
token_data = my_api.useAuth('Bearer', response['data'].split('"')[3])
print 'New Token Data- ' + str(token_data)
print 'Fetching User List ...'
print '\n'
print my_api.get({'endpoint':'marketers'})['data']
print '\n Thank you ...'
