#!/usr/bin/python3
import json
import random
import statistics
import sys
import ast

#inputs=input()
inputs=sys.stdin.read()
paramsliteralinputs=ast.literal_eval(inputs)
paramsloadedinputs=json.loads(inputs)
#inputs = sys.argv[1]
#inputs = ""

#params = json.loads(inputs)
#inputs = input() #sys.stdin.read()
# Assuming params_json contains the JSON string
#inputs = event["inputs"]

#params = json.loads(inputs)
#params = params['inputs']
#data = params['data']
#minhistory = params['minhistory']
#shots = params['shots']
#buy_sell = params['buy_sell']
#results = []

#for i in range(minhistory, len(data['Buy'])):
#    if buy_sell == "Buy" and data['Buy'][i] == 1:  # if we're interested in Buy signals
#        subset_close = data['Close'][i - minhistory:i]

        #Calculate mean and standard deviation
#        changes = [subset_close[j] / subset_close[j-1] - 1 for j in range(1, len(subset_close))]
#        mean = statistics.mean(changes)
#        std = statistics.stdev(changes)

        # Generate much larger random number series with the same broad characteristics
#        simulated = [random.gauss(mean, std) for x in range(shots)]

        # Sort and pick 95% and 99%
#        simulated.sort(reverse=True)
#        var95 = simulated[int(len(simulated) * 0.95)]
#        var99 = simulated[int(len(simulated) * 0.99)]
        #print(var95, var99)  # so you can see what is being produced
#        results.append([data['Date'][i], var95, var99])
        
#    elif buy_sell == "Sell" and data['Sell'][i] == 1: #if we're interested in Sell signals
#        subset_close = data['Close'][i - minhistory:i]

        # Calculate mean and standard deviation
#        changes = [subset_close[j] / subset_close[j-1] - 1 for j in range(1, len(subset_close))]
#        mean = statistics.mean(changes)
#        std = statistics.stdev(changes)

        # Generate much larger random number series with the same broad characteristics
#        simulated = [random.gauss(mean, std) for x in range(shots)]

        # Sort and pick 95% and 99%
#        simulated.sort(reverse=True)
#        var95 = simulated[int(len(simulated) * 0.95)]
#        var99 = simulated[int(len(simulated) * 0.99)]
        #print(var95, var99)  # so you can see what is being produced
        #results.append((data['Date'][i], var95, var99))
#        results.append([data['Date'][i], var95, var99])
print("Content-Type: text/html;charset=utf-8")
print("")
print("----------JUST INPUTS--------------")
print(str(type(inputs)))
print(str(inputs))
print("----------JUST INPUTS--------------")
print("----------LITERAL EVAL INPUTS--------------")
print(str(params))
print(str(type(params)))
print("-----------LITERAL EVAL INPUTS-------------")
print("-----------JSON LOADED INPUTS-------------")
print(str(paramsloadedinputs))
print(str(type(paramsloadedinputs)))
print("-----------JSON LOADED INPUTS-------------")
