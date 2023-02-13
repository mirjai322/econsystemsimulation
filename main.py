# from agents import *




print("Hi Miraya, this is Sam. We will do our coding here.")

# Write a for loop that prints only even numbers up to some number N
# N=10
# for i in range(0, N): #set arbitrary value for N
#   if(i%2 == 0):
#     print(i)

# Write a function that takes as input a string and returns if there is a vowel in it.
sam_string = "asdfjkzsd;jfaiwe"
sam_string2 = 'kkllldffdsdf'

def function_name():
  array = list(sam_string)




##############################################################

a=  [1,2,3,2] # list
b = set(a)
print(a, b)
c = {}
a = "Sam"
b = "Miraya"
c = "Vijay"

call_log = [a,b,c]

better_call_log = {}
better_call_log[a] = [1,2,3]
better_call_log[b] = [1,2,2,2,2]
better_call_log[c] = [1,2,3,1,1]

# print(better_call_log["Vijay"])
# print(better_call_log)

better_call_log["Sam"] = {"friends": [1,1,1,],
                         "family": [1,2,3],
                         "strangers": []}
# # print(better_call_log)
# print()
# print(better_call_log["Sam"]["friends"])

config = {
  "environment": {
    "num_agents": 10,
    "num_firms": 5,
  },
  "agents": {
    "risk_range": [0,0.2],
    
  },
  "firms": {}


  
}

import numpy as np 

print(np.random.rand() < 0.5 )
