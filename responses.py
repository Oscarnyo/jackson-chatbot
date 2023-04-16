import random
import sensor
from sensor import *
from turning_egg_fuzzy import *
from HatchRate import *
from advice import *


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

Chicken = ['chicken egg', 'Give me the good advice for hatching chicken eggs', 'chicken', 'chicken eggs', 'chicken egg haching advice', 'chicken egg tips', 'chicken egg good practice', 'chicken egg']

Duck = ['duck egg', 'Give me the good advice for hatching duck eggs', 'duck', 'duck eggs', 'duck egg haching advice', 'duck egg tips', 'duck egg good practice', 'duck egg']

Ostrich = ['ostrich egg', 'Give me the good advice for hatching ostrich eggs', 'ostrich', 'ostrich eggs', 'ostrich egg haching advice', 'ostrich egg tips', 'ostrich egg good practice', 'ostrich egg']

Peafowl = ['peafowl egg', 'Give me the good advice for hatching peafowl eggs', 'peafowl', 'peafowl eggs', 'peafowl egg haching advice', 'peafowl egg tips', 'peafowl egg good practice', 'peafowl egg']

Pigeon = ['pigeon egg', 'Give me the good advice for hatching pigeon eggs', 'pigeon', 'pigeon eggs', 'pigeon egg haching advice', 'pigeon egg tips', 'pigeon egg good practice', 'pigeon egg']

Turkey = ['turkey egg', 'Give me the good advice for hatching turkey eggs', 'turkey', 'turkey eggs', 'turkey egg haching advice', 'turkey egg tips', 'turkey egg good practice', 'turkey egg']


rude = ['noob','stupid']



others = ['...','I dont know, go ask your chatgpt', 'I dont know bro', 'emmm..', 'Sorry, I do not understand','(0_0)Y']



def get_response(message: str) -> str:
    # Greetings
    
    message = message.lower() 
    if any(word in message for word in Chicken):
        return str(chicken())
    
    if any(word in message for word in Duck):
        return str(duck())
    
    if any(word in message for word in Ostrich):
        return str(ostrich())
    
    if any(word in message for word in Peafowl):
        return str(peafowl())
    
    if any(word in message for word in Pigeon):
        return str(pigeon())
    
    if any(word in message for word in Turkey):
        return str(turkey())
    
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
