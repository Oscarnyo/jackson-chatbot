import random
import sensor
from weather import *
from sensor import *
from turning_egg_fuzzy import *
from HatchRate import *


greetings = ['hi', 'hello', 'whatsup']
end = ['bye', 'goodbye']
ask = ['you doing', 'doing good']
thanks = ['thanks', 'thank']

temperature = ['temperature', 'temp']
humidity = ['humidity', 'humid']
turning_egg = ['turning eggs', 'egg turn', 'turning egg', 'need to be turn','turn']
day = ['current day', 'current days']
status = ['incubator status','status', 'all', 'latest status']
hatch = ['hatch rate', 'successful rate']




rude = ['noob']



others = ['...','I dont know, go ask your chatgpt', 'I dont know bro', 'emmm..', 'Sorry, I do not understand','(0_0)Y']



def get_response(message: str) -> str:
    # Greetings
    
    message = message.lower()
    if any(word in message for word in greetings):
        return str('Hello, I am Jackson, an Egg Incubating Chat-Bot.')

    if any(word in message for word in end):
        return str('See you!')

    if any(word in message for word in ask):
        return str('Im doing fine!')

    if any(word in message for word in thanks):
        return str('You are welcome!')
    
    if any(word in message for word in rude):
        return str('https://tenor.com/blOLy.gif')
    
    # Temperature
    if any(word in message for word in temperature):
        return str(show_temp())

    # Humidity
    if any(word in message for word in humidity):
        return str(show_humid())
    
    #day
    if any(word in message for word in day):
        return str(show_day())
    
    #Get All
    if any(word in message for word in status):
        return str(getAll())
    
    #Hatch Rate
    if any(word in message for word in hatch):
        return str(get_hatch_rate())
    
    
    
    #turning egg
    
    if any(word in message for word in turning_egg):
        return str(getTurning())
    
    
    

    

        

    

    return random.choice(others)