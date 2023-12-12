# Making a GET request
import requests as RQ

r = RQ.get('https://api.github.com/users/naveenkrnl')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)