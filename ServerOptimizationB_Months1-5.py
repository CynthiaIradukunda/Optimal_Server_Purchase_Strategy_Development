# -*- coding: utf-8 -*-
"""
Created on Wed May  1 05:11:38 2024

@author: Cynthia Iradukunda
"""
from pulp import *

# Define the problem
prob = LpProblem("Server_Purchasing_Plan", LpMinimize)

# Months and server types
months = range(1, 6)
server_types = ["Standard_PC", "Enhanced_PC", "SGI_Workstation", "Sun_Workstation"]
server_capacity = {"Standard_PC": 30, "Enhanced_PC": 80, "SGI_Workstation": 200, "Sun_Workstation": 2000}
server_cost = {"Standard_PC": 2500, "Enhanced_PC": 5000, "SGI_Workstation": 10000, "Sun_Workstation": 25000}
employees_needed = {1: 0, 2: 50, 3: 180, 4: 30, 5: 70}

# Decision variables for server purchases
x = LpVariable.dicts("Server_Purchase",
                        [(m, s) for m in months for s in server_types],
                        lowBound=0, cat='Integer')

# Variable for tracking cumulative employees covered
cumulative_employees_covered = LpVariable.dicts("Cumulative_Covered_Employees",
                                                    months,
                                                    lowBound=0, cat='Continuous')

# Objective: Minimize total cost including potential discounts
prob += lpSum([x[(m, s)] * server_cost[s] * (0.9 if s == "SGI_Workstation" and m in [1, 2] else 
                  0.75 if s == "Sun_Workstation" and m in [1, 2] else 1.0) 
                  for m in months for s in server_types])

# Budget constraint for the first two months
prob += lpSum([x[(m, s)] * server_cost[s] for m in [1, 2] for s in server_types]) <= 9500

# Constraints for cumulative employees covered
for m in months:
    if m == 1:
        # First month, cumulative coverage equals this month's purchases
        prob += cumulative_employees_covered[m] == lpSum([x[(m, s)] * server_capacity[s] for s in server_types])
    else:
        # Subsequent months, add this month's coverage to previous months
        prob += cumulative_employees_covered[m] == (cumulative_employees_covered[m - 1] + 
                                                    lpSum([x[(m, s)] * server_capacity[s] for s in server_types]))
    
    # Ensure coverage meets or exceeds the number of employees needed
    prob += cumulative_employees_covered[m] >= employees_needed[m]

# High-capacity server requirement from month 3

for m in months:
    if m == 1:
        # First month, cumulative coverage equals this month's purchases
        prob += lpSum([x[(m, s)] for s in ["SGI_Workstation", "Sun_Workstation"]]) >= 1
    elif m == 3:
        prob += lpSum([x[(m, s)] for s in ["SGI_Workstation", "Sun_Workstation"]]) >= 1

# Solve the problem
prob.solve()

# Output the results
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

print("Total Cost: $", value(prob.objective))