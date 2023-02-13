"""
simulate() is the main driver. It will instantiate the Economy environment and different types of agents like Individuals, Firms and Regulators. In each iteration, it will ask agents to perform various actions. Each action will result in a new state and rewards. Cumulative reward will be calculated?. 
"""
from environment import Economy
from agents import Econ
from firms import Firm
from rewards import *
import sys

config = {
  "agents": {
    "num_agents":10,
    "agent_action_space": ['invest'],
    "agent_state_space": ['money'], # Name of variable
    "reward_function": ["money_agents"],
  },
  "firms": {
    "num_firms": 3,
    "firm_action_space":['fee_rate'],
    "firm_state_space": ['money'],
    "reward_functions": ["money_firms"],
  },
  "regulators": {
    "num_regulators": 1, # Leave as 1, there is just 1 gov.
    "reg_action_space":['fee_rate', 'tax_rate'],
    "tax_rate_agents": 0.10,
    "tax_rate_firms": 0.20,
    "reg_state_space": ['wealth_equality', 'money'],
    "reward_functions": ['money_firms_agents','equality_agents']
    # Equality could be measured by the standard deviation of agents (smaller is better). Could make this a negative number
  },
  
}

def simulate(config, num_iterations):

  # Set up environment and agents
  # Rewards is embedded into each of these objects
  enviroment = Economy(config)
  environment.configure_agents()
  environment.configure_firms()
  environment.configure_regulators()
# start with some inital values for the networth of each inddiv and firm 
  
  for i in range(num_iterations):
    # Do something

    # Agents interact with each other
    environment.interact_agents_with_agents()
    
    # Agents interact with firms
    environment.interact_firms_with_agents()

    # Firms interact with firms
    environment.interact_firms_with_firms()

    # Government regulate firms (maybe penalize)
    environment.regulators_regulate_firms()

    #Government regulate individuals
    environment.regulators_regulate_agents()
    
    # Change regulations (if needed) (Goverment reward and response)
    environment.change_regulations()

    # Modulo operator = "remainder operator"
    if ((i+1) % config['general']['save_state_iterations'] ==0):
      environment.save_state() #is this for recording the values


##################
simulate(config,20)
  


"""
MDP = {G, A, S, R} #G = agent
G = {g1, g2, g3} = {individuals, firms, government}

A_g1 = A_{individuals} = {...}
A_g2 = A_{firms} = {...}
A_g3 = A_{government} = {...}

S_g1 = S_{individuals} = {...}
S_g2 = S_{firms} = {...}

R_g1 = R_{individuals} = {...}
R_g2 = R_{firms} = {...}

Policy = probability distribution of actions, given a state
\pi_g1(a|s) = policy for individuals, given a state
\pi_g2(a|s) = policy for firms, given a state

Dynamics / model / world model = The end state of your agent (individual, firm) after they have conducted an action
- e.g. If I bet $100 with someone else, what happens next?

"""
  
example = """
S = {money}
A_g1 = {bet/invest} -> the amount (or percent) you bet can vary
A_g2 = {fulfill_transaction} -> Can vary fees

Reward: 
R_g1 = {winning} 
R_g2 = {more money}

Policy:
- The policy for individuals is betting a higher percentage of wealth if they have more. Also, if someone has less money than you, you can match their bets more often. Therefore, you might bet more often than another.
- The policy for firms is set fees to maximize profit.
- The policy for government is to tax individuals based on what tax bracket they fall into, and they regulate firms by limiting the fees they can charge.

Dynamics:
*Betting is randomized, come up with function (perhaps based on risk appetite value)
- For agent: If they win the bet, they keep their current wealth + add the amount that the other person betted. If they take out a loan, they pay the fees and interest associated.
---Maybe if they win the bet they are likely to bet again? Increase in risk appetite?
- For firms: They earn fees every transaction, and it is based on how many people are taking out loans as well as the value of the loans.


"""