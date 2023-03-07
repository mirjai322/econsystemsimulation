"""
Tasks Completed [ Feb 13]: 
================
1. configured .replit file to run simulation.py instead of main.py
2. configure_agents, configure_firms, configure_regulator
3. save_state and print_state to print the current state of the environment in .csv format. 
4. added logic to interact-agent-with-agent (bet amount depends on the networth )
5. added logic to interact-agent-with-firms for loans. Added Ledger to keep track of all the loan transactions between agents and firms
6. Printing stats for agents , firms using numpy arrays

Tasks Completed [ Feb 20]
=================
1. added logic to setting loan amount bank is willing to offer to agent, and carrying out loan
  + tested and adjusted to deal with borderline cases
2. configured regulator income (and added attribute to class)
3. wrote logic for merger between 2 firms (firm-firm interaction)
4. wrote logic for spinoff (1 firm breaks into 2) (firm-firm interaction)
5. added conditions where bet will not take place (agent-agent interaction)
6. wrote regulation of agents (implemented tax bracket system) logic (regulator-agent interaction)
7. wrote logic of regulators taxing firms (regulator-firm interaction)

Tasks Completed [Feb 27]
=======================
1. Implemented weighted random for agent choosing firm
2. Added code to run the simulation N times and generate csv for each run with a unique name (detailed_data_iteration_0.csv, detailed_data_iteration_1.csv ...etc)
3. Added code to create a single summary.csv file that summarizes all the stats for "agents" and "firms" for each simulation run 
4. modify code to first run centralized simulation (say 50 runs with 1000 iterations in each run), then run decentralized simulation with (say 50 runs and 1000 iterations in each run)
5. Creating all csv files in a seprate folder "centralized_output" and "decentralized_output" to keep the code separate from the output files and keep centralized files separate from decentralized. 
6. Environment now has 2 modes (is_centralized true or false)
7. Write the code for decentralized simulation
  - Firm method is to route/connect 2 Agents:
    - 1 agent is loan seeker
    - 1 agent is loan provider
    * There is protocol for "general oversight"
  - Every agent can be a provider but they have "reputation" for the prices they set, and based on the fees they set they can either get more or less loan seekers
    - Reputation can be an attribute based on 

NEXT STEPS:
- add "loan_boundary" attribute to each agent
- for each loan:
  - choose agentLending based on whether loan_amount falls into loan_boundary
    - if the random choice of agentLending does not match (loan_amount is not within loan_boundary), choose different agent
  - agentLending sets a fee/rate
- add regulation thru taxes (regulator -> agents, regulator -> firms)
- add regulation thru oversight ()

Current Focus Task:[ Feb 14]
Agent bets with Agents:
- How much will an individual bet?
  + Based on the "income bracket" the individual falls in, they will bet a certain percentage of their net worth. Likely the higher their networth, they will be willing to bet a higher percentage of their net worth; lower net worth = lower percentage.

- Is there a time where the individual will choose not to bet?
  + If the individual is below a certain networth value (includes bankruptcy), they will bet 0 dollars.
  + There are probably pairings where one individual doesn't stand to gain much.
    + If they are betting with an individual that has a networth below a certain point, they may choose not to bet as there is no benefit commensurate to the resources used.


Plan to do following next: 
============================

-- add the interactions into methodology
3. Work on rewards? 
5. start writing decentralization algorithms
6. handle boundary condition (agents net worth goes below 0)

Big picture
===========
Created an environment, added agents+firms, some real life transactions happening that is affecting the balance sheet of agents and firms. 
what is next? 







___________________________________________________
    
* interact_firms_with_firms
    Merger:
    1. Create new firm
    2. Set net worth equal to sum of 2 other firm's net worths
    3. Delete 2 original firms
__________________________________________________
* regulators_regulate_firms
    #written in rewards??
__________________________________________________
* regulators_regulate_agents
    #written in rewards??
__________________________________________________
* change_regulations
    * 
__________________________________________________
* reg_money_firms_agents
    #written in rewards, but need to make sure its updating when the simulation runs
__________________________________________________
* equality_agents
    #written in rewards, but need to make sure its updating when the simulation runs
__________________________________________________
* money_agents
    #written in rewards, but need to make sure its updating when the simulation runs
__________________________________________________
* investment_payout
    * ?
__________________________________________________
* bankruptcy
    * ?
________
Time stamps

"""

sams_notes = """

What has been done:
- Base structure of the simulation complete
- Several decisions regarding agent, firm, regulator action/state spaces

Things to think about:
- Can you make decisions in the action space as simple and atomic as possible.
- If you went in front of a group of economists and gave a talk on these simulations, how would you justify your choices?
  + For example, how should a firm determine the interest rate if offers an individual?
  + When might a bank just refuse a loan?
  + Keep action spaces relatively small and for EACH action, make the decisions as realistic as possible.

Firm loans to Agents:
- Who will a firm approve a loan for? What matters here?
  + If there is a credit score attribute for each individual, then credit score must be higher than a "minimum amount" in order for that individual to take out a loan from the firm. This is to prevent defaulting, which loses money for the firm.
  + Realistically, firms will not approve loans for people who are under a certain credit score, so that action will be limited for those certain individuals.
- How will a firm set interest rates for a loan?
  + It will be based on the net worth of the individual taking out the loan - as if in a bracketed system where it is x% if the net worth between a & b, y% between c & d, etc
  + The rates that other firms are charging
  + Maximize profits - minimum rate so they are not losing money or making 0 profit, and maximum rate that is set by government
  + Calculate based on market share of firm - sum up net worths of each firm and what percentage of total net worth that is, that percentage would be how much loan money they are lending
- How will a firm decide if the maximum loan it would offer a person?
  + The net worth of the individual
  + The profit they will make off the interest rate on that loan (larger loan = smaller interest rate)
  + Size/networth of bank
  
Agent bets with Agents:
- How much will an individual bet?
  + Based on the "income bracket" the individual falls in, they will bet a certain percentage of their net worth. Likely the higher their networth, they will be willing to bet a higher percentage of their net worth; lower net worth = lower percentage.

- Is there a time where the individual will choose not to bet?
  + If the individual is below a certain networth value (includes bankruptcy), they will bet 0 dollars.
  + There are probably pairings where one individual doesn't stand to gain much.
    + If they are betting with an individual that has a networth below a certain point, they may choose not to bet as there is no benefit commensurate to the resources used.


Government regulations agents:
- What is the taxing system?
  + If the agent falls between the minimum and mean of the Agent Stats, then they will be taxed 15% of their net worth every 12 iterations (considering 1 iteration = 1 month)
  + If the agent falls between mean and maximum, they are taxed 25% of net worth

Government regulations firms:
- What is the taxing system?
  + 15% base rate, 20% for those above the mean
- How will the government prevent monopolies?





"""

# Pseudo-code for weighted random selection

# firm_weights_raw = np.array([firm.net_worth for firm in firms])
# firm_weights =firm_weights_raw/firm_weights_raw.sum()

# agent_firm_choice = np.random.choice(range(firm_weights.shape[0]),
#                                     p=firm_weights)
'''
Decentralized interactions
- agents interact with agents
  + can borrow money from other individuals?
- agents interact with firms
  + agents decide on and set fees
- regulating firms
- regulating individuals
  + 


Sam's  thoughts:
- Make the firm for decentralized finance a "router"
- a.k.a., when someone wants a loan or service, the "firm" simply puts them in contact with a set of people that could do that form them
- Those people are other agents!!
- The "firm router" should have a protocol for general oversight
- agents to firms is really agents to agents with some rules.
- As far as regulation of the "firms", this is now regulation on the agents!
  + The regulators also can change the protocol for the firm itself (the router).

Next Steps:
- For agents choosing firms, make the choice a weighted random choice.
- For centralized simulation, run for 1000 iterations and collect all data. 
  + Repeat this process 50-100 times. Name each of the output csvs differently.
- For decentralized systems, finish building and testing the code.
  + The simulations of this can wait until next week

'''

"""
Questions: 
- What to do about change_regulations() function? Because varying regulatory conditions is a part of the paper
"""
