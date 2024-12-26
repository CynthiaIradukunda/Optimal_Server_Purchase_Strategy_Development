# -*- coding: utf-8 -*-

########################## Case Study 1 - Month 5 #############################

from pulp import *

# Available Data
server_types = ['Standard_Intel_Pentium_PC',
                'Enhanced_Intel_Pentium_PC',
                'SGI_Workstation',
                'Sun_Workstation']
# This might be used directly without this array
discount_percentages = [0.10, 0.25]

# Dictionaries
server_capacity = {
    'Standard_Intel_Pentium_PC': 30,
    'Enhanced_Intel_Pentium_PC': 80,
    'SGI_Workstation': 200,
    'Sun_Workstation': 2000
}

server_capacity_list = [0, 30, 80, 200, 2000]

server_cost = [2500, 5000, 10000, 25000]
cumulative_number_employees = {1: 0, 2: 50, 3: 230, 4: 260, 5: 330}
cumulative_number_employees_covered_soFar = 260  #From months 1&2&3 {0 + 2 Standard_Intel_Pentium_PC (30*2) + 1 SGI Workstation (200)}

# Discounts
discounts = [0.10, 0.25]

# Setting the problem variable
prob = LpProblem('Server_Month5', LpMinimize)

# Setting our Decision Variables
s1 = LpVariable("Standard_Intel_Pentium_PC", lowBound=0, cat="Integer")
s2 = LpVariable("Enhanced_Intel_Pentium_PC", lowBound=0, cat="Integer")
s3 = LpVariable("SGI_Workstation", lowBound=0, cat="Integer")
s4 = LpVariable("Sun_Workstation", lowBound=0, cat="Integer")


# Objective Function
prob += s1 * server_cost[0]*2 + s2 * server_cost[1] + s3 * server_cost[2]*1 + s4 * server_cost[3]

# Constraints

# 1. Server capacity
prob += server_capacity['Standard_Intel_Pentium_PC']*s1 + server_capacity['Enhanced_Intel_Pentium_PC']*s2 + \
    server_capacity['SGI_Workstation']*s3 + \
    server_capacity['Sun_Workstation']*s4 >= cumulative_number_employees[5] - cumulative_number_employees_covered_soFar , "Server_Capacity_Month5"
    
print(prob)

# Solve the Problem
prob.solve()
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

# Print the optimized total cost
print("Optimized Total Cost - Month 5: $", value(prob.objective))

###############################################################################
