from agents import  Agent
from firms import Firm
from regulators import Regulator
from numpy import random
from environment import Economy


config = {
    "agents": {
        "num_agents": 10,
        "agent_action_space": ['invest'],
        "agent_state_space": ['money'],  # Name of variable
        "reward_function": ["money_agents"],
    },
    "firms": {
        "num_firms": 3,
        "firm_action_space": ['fee_rate'],
        "firm_state_space": ['money'],
        "reward_functions": ["money_firms"],
    },
    "regulators": {
        "num_regulators": 1,  # Leave as 1, there is just 1 gov.
        "reg_action_space": ['fee_rate', 'tax_rate'],
        "tax_rate_agents": 0.10,
        "tax_rate_firms": 0.20,
        "reg_state_space": ['wealth_equality', 'money'],
        "reward_functions": ['money_firms_agents', 'equality_agents']
        # Equality could be measured by the standard deviation of agents (smaller is better). Could make this a negative number
    },
    "general":{
        "save_state_iterations":10
    }

}

def simulate(config, num_iterations):
    environment = Economy(config)
    environment.configure_agents()
    environment.configure_firms()
    environment.configure_regulators()

    # starting from i instead of 0 just for convenience
    for i in range(1,num_iterations+1):
        # Agents interact with each other
        environment.interact_agents_with_agents()

        # Agents interact with firms
        environment.interact_firms_with_agents()

        # Firms interact with firmsooo
        environment.interact_firms_with_firms()

        # Government regulate firms (maybe penalize)
        environment.regulators_regulate_firms()

        # Government regulate individuals
        environment.regulators_regulate_agents()

        # Change regulations (if needed) (Goverment reward and response)
        environment.change_regulations()

        # Modulo operator = "remainder operator"
        if (i== 1 or i== num_iterations or (i) % config['general']['save_state_iterations'] == 0):
            environment.save_state(i)
    # all iterations done -- now print the state to a csv file for further analysis
    environment.print_state()


#########################
# Invoke simulation
#########################
simulate(config,40)

