import json

import requests

booking_id = 17
response = requests.get('https://restful-booker.herokuapp.com/booking/{}'.format(booking_id),
             params={'id': '17'},headers={'Accept': 'application/json'})

print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
dict_response['firstname'] !='Nafis'
#assert dict_response['firstname'] =='F18'
print(dict_response['firstname'] =='F18')
print(dict_response['firstname'] !='Nafis')
json_response = response.json()
print(json_response)
print(type(json_response))
print(response.status_code == 200)
print(response.headers)
print(type(response.headers))
print(response.headers['Content-Type']== 'application/json; charset=utf-8')