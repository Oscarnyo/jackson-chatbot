import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import sensor
from skfuzzy import control as ctrl



# establishing fuzzy logic for getting a good range of data
humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')
temp = ctrl.Antecedent(np.arange(0, 51, 1), 'temp')
turning = ctrl.Consequent(np.arange(0, 11, 1), 'turning')

humidity['too dry'] = fuzz.trapmf(humidity.universe, [0, 0, 41, 51])
humidity['well'] = fuzz.trapmf(humidity.universe, [51, 63, 75, 87])
humidity['too wet'] = fuzz.trapmf(humidity.universe, [87, 95, 100, 100])

temp['too cold'] = fuzz.trapmf(temp.universe, [0, 0, 27, 34])
temp['moderate'] = fuzz.trimf(temp.universe, [34, 38, 41])
temp['too hot'] = fuzz.trapmf(temp.universe, [41, 44, 50, 50])

turning['few'] = fuzz.trimf(turning.universe, [0, 0, 5])
turning['moderate'] = fuzz.trimf(turning.universe, [0, 5, 10])
turning['many'] = fuzz.trimf(turning.universe, [5, 10, 10])

rule1 = ctrl.Rule(temp['too cold'] & humidity['too dry'], turning['many'])
rule2 = ctrl.Rule(temp['too cold'] & humidity['well'], turning['moderate'])
rule3 = ctrl.Rule(temp['too cold'] & humidity['too wet'], turning['few'])
rule4 = ctrl.Rule(temp['moderate'] & humidity['too dry'], turning['many'])
rule5 = ctrl.Rule(temp['moderate'] & humidity['well'], turning['moderate'])
rule6 = ctrl.Rule(temp['moderate'] & humidity['too wet'], turning['few'])
rule7 = ctrl.Rule(temp['too hot'] & humidity['too dry'], turning['few'])
rule8 = ctrl.Rule(temp['too hot'] & humidity['well'], turning['few'])
rule9 = ctrl.Rule(temp['too hot'] & humidity['too wet'], turning['few'])

turning_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

turning_simulation = ctrl.ControlSystemSimulation(turning_ctrl)


def getTurning():
    
    turning_simulation.input['temp'] = float(sensor.gettemp())
    turning_simulation.input['humidity'] = float(sensor.gethumid())
    

    turning_simulation.compute()
    output = int(turning_simulation.output['turning'])
    return f"The number of times of the eggs turning are {output}"
    # return f'''The number of times of the eggs are turning are {turning_simulation.output['turning']}'''
    
    
