import requests
from pprint import pprint
api_key='618e1ac9f4d0caaba6cdb4913a7c018e'
def get_weather_data(city):
    #units=metric gives the temperature in degree Celsius
    url='https://api.openweathermap.org/data/2.5/weather?appid='+api_key+'&q='+city+'&units=metric'
    #Using the above API te¥he data can be retrieved in JSON, XML and HTML format
    weather_data=requests.get(url).json()
    return(weather_data)

def main():
    city=input("Enter the city name>>")
    print(f"the name of the city is {city}")   
    get_weather_data(city,api_key)

#The below condition is added to avoid the execution of the code when it is imported as module

if __name__ == '__main__':
    main()