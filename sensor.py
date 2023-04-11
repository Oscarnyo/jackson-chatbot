import requests



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

############### Temperature ############
def show_temp():
    return f'''Current temperature will be at {+ gettemp()}°C'''


##############Humidity#################
def show_humid():
    return f'''Current humidity is {gethumid()}%'''


def show_day():
    return f'''is Day {int(getDay())} of the egg hatching process'''