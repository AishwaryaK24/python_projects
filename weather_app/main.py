import requests
from pprint import pprint

city=input("Enter the city name>>")
api_key='618e1ac9f4d0caaba6cdb4913a7c018e'
#units=metric gives the temperature in degree Celsius
url='https://api.openweathermap.org/data/2.5/weather?appid='+api_key+'&q='+city+'&units=metric'
#Using the above API te¥he data can be retrieved in JSON, XML and HTML format
weather_data=requests.get(url).json()
pprint(weather_data)