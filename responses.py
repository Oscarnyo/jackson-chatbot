import random
from weather import *
from sensor import *


greetings = ['hi', 'hello', 'whatsup']
end = ['bye', 'goodbye']
ask = ['you doing', 'doing good']
thanks = ['thanks', 'thank']


current_weather = ['info', 'information']
temperature = ['temperature', 'temp']
humidity = ['humidity', 'humid']

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

    

        

    

    return random.choice(others)