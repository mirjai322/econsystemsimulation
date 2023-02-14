"""
Tasks Completed: 
================
1. configured .replit file to run simulation.py instead of main.py
2. configure_agents, configure_firms, configure_regulator
3. save_state and print_state to print the current state of the environment in .csv format. 
4. added logic to interact-agent-with-agent (bet amount depends on the networth )
5. added logic to interact-agent-with-firms for loans. Added Ledger to keep track of all the loan transactions between agents and firms
6. Printing stats for agents , firms using numpy arrays

Plan to do following next: 
============================

1. add firm-to-firm-interaction logic related to merger 
2. add some logic for regulator's role 
3. Work on rewards? 

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




"""