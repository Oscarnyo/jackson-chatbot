import requests
import pytz
from datetime import datetime

api_url = 'http://api.weatherstack.com/forecast'
api_key = '98093e2db8dfa46bf871aabd5926b659'
api_city = 'Batu Kawan'
response = requests.get(api_url + '?access_key=' + api_key + '&query=' + api_city)

weatherApi = response.json()


######################################### Weather #######################################################
def weather():
    return f'''Current temperature will be at {+ getTemp()}°C, and humidity is {getHumidity()}%. Current time is {get_time()}'''


def getTemp():
    return weatherApi['current']['temperature']


def getHumidity():
    return weatherApi['current']['humidity']


def getCloudcover():
    return weatherApi['current']['cloudcover']



# Get time of day
def get_time():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    time = now.strftime("%H:%M:%S")
    if now.hour < 12:
        time += ", Morning"
    elif now.hour < 17:
        time += ", Afternoon"
    elif now.hour < 19:
        time += ", Evening"
    else:
        time += ", Night"
    return time


############### Temperature ############
def show_temp():
    return f'''Current temperature will be at {+ getTemp()}°C'''


##############Humidity#################
def show_humid():
    return f'''Current humidity is {getHumidity()}%'''