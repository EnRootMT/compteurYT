import requests
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=strasbourg&appid=CLE_API&units=metric'
responsemeteo = requests.get(url)
data = json.loads(responsemeteo.text)
print(data)

temp = data['main']['temp']
tempdisplay = str(temp)+"°C"
print(tempdisplay)
