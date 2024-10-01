import requests 

#request = requests.get('https://openweathermap.org/api')
request = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={7d2fa2adbcb9eec66ccb3ddebb890501}')




# success code - 200 
print(request)

# print the content of the request 
print(request.content)