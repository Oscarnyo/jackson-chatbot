import pandas as pd

def get_good_practice(egg_type):

    df = pd.read_csv('Eggs.csv')
    mask = df['Egg_Type'] == egg_type.capitalize()
    good_practice = df.loc[mask, 'Good_Practice'].values
    if len(good_practice) == 0:
        return None
    else:
        return good_practice[0]

#Use the function above
good_practice = get_good_practice('cHicken')
print(good_practice) 
