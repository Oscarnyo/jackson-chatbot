import pandas as pd

def get_good_practice(egg_type):

    df = pd.read_csv('Eggs.csv')
    mask = df['Egg_Type'] == egg_type.capitalize()
    good_practice = df.loc[mask, 'Good_Practice'].values
    if len(good_practice) == 0:
        return None
    else:
        return good_practice[0]

# #Use the function above
# good_practice = get_good_practice('Chicken')
# print(good_practice) 

def chicken():
    good_practice = get_good_practice('Chicken')
    return good_practice

def duck():
    good_practice = get_good_practice('Duck')
    return good_practice

def ostrich():
    good_practice = get_good_practice('Ostrich')
    return good_practice

def peafowl():
    good_practice = get_good_practice('Peafowl')
    return good_practice

def pigeon():
    good_practice = get_good_practice('Pigeon')
    return good_practice

def turkey():
    good_practice = get_good_practice('Turkey')
    return good_practice
