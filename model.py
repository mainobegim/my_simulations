import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm

#Parameters
today=15
threshold=13
std = 3
cost_of_covering = 10
cost_of_loss = 100
total_cost = 0
random_total_cost= 0 
smart_costs_daily=[]
random_costs_daily=[]
smart_costs_sims=[]
random_costs_sims=[]
counter = 0

#Repeat for 365 days
for day in range(365):
    today += np.random.normal(0,3)
    probability = norm.cdf(threshold,today,std)
    expected_cost_not_covering = probability * cost_of_loss
    expected_cost_covering = cost_of_covering
    
    #Logic for smart decision
    if expected_cost_not_covering>expected_cost_covering:
        #print('cover the crops')
        total_cost += expected_cost_covering

    else:
        #print('dont cover the crops')
        total_cost += expected_cost_not_covering

    #Logic for random decision
    random_output = random.randint(0,1)
    if random_output==0:
        random_total_cost += expected_cost_not_covering
        #print('dont cover the crops')
        
    else:
        random_total_cost += expected_cost_covering
    
    smart_costs_daily.append(total_cost)
    random_costs_daily.append(random_total_cost)

#Plotting the line graph
plt.figure(1)
plt.plot(smart_costs_daily, label = 'Smart Strategy')
plt.plot(random_costs_daily, label = 'Random Strategy')
plt.xlabel('days')
plt.ylabel('costs')
plt.legend()

#Repeat the simulation 1000 times
for _ in range(1000):
    today = 15   #reset
    total_cost = 0    #reset
    random_total_cost= 0     #reset
    #Repeat for 365 days
    for day in range(365):
        today += np.random.normal(0,3)
        probability = norm.cdf(threshold,today,std)
        expected_cost_not_covering = probability * cost_of_loss
        expected_cost_covering = cost_of_covering
    
        #Logic for smart decision
        if expected_cost_not_covering>expected_cost_covering:
            #print('cover the crops')
            total_cost += expected_cost_covering

        else:
            #print('dont cover the crops')
            total_cost += expected_cost_not_covering

        #Logic for random decision
        random_output = random.randint(0,1)
        if random_output==0:
            random_total_cost += expected_cost_not_covering
            #print('dont cover the crops')
        
        else:
            random_total_cost += expected_cost_covering

    if total_cost<random_total_cost:
        counter+=1
    
    #Add data to the empty lists
    smart_costs_sims.append(total_cost)
    random_costs_sims.append(random_total_cost)
    

#Final results
print(f'Smart strategy total cost: £{total_cost:.2f}')
print(f'Random strategy total cost: £{random_total_cost:.2f}')
print(f'Smart strategy saved: £{random_total_cost-total_cost:.2f}')
print(f'Smart beats random {counter} times out of 1000 simulations')


#Plotting the histogram
plt.figure(2)
plt.hist(smart_costs_sims, label='Smart Strategy Costs', alpha = 1)
plt.hist(random_costs_sims, label='Random Strategy Costs', alpha = 0.5)
plt.xlabel('total cost')
plt.ylabel('number of the times')
plt.legend()

plt.tight_layout()
plt.show()
 