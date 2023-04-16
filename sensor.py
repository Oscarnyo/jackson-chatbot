import requests
import datetime
import pytz



response = requests.get("https://eggincubator-825e1-default-rtdb.firebaseio.com/.json")
data = response.json()
temperature = float(data['Temperature'])
humidity = float(data['Humidity'])
day = float(data['Day'])


def getDay():
    return day

def gettemp():
    return temperature

def gethumid():
    return humidity

def getTemp_Humid():
    return temperature, humidity

def getTime():
    return datetime.datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M")

def getAll():
    return f'Current temperature: {gettemp()}°C\n' \
           f'Current humidity: {gethumid()}%\n' \
           f'Is Day {int(getDay())} of the egg hatching process\n' \
           f'Last Updated: {getTime()}'

############### Temperature ############
def show_temp():
    return f'''Current temperature is {+ gettemp()}°C'''


##############Humidity#################
def show_humid():
    return f'''Current humidity is {gethumid()}%'''


def show_day():
    return f'''Is Day {int(getDay())} of the egg hatching process'''