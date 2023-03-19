from agents import Agent
from firms import Firm
from regulators import Regulator
from numpy import random
from environment import Economy
import shutil
import os
import csv
'''
config is used to configure simulation. You can control how many agents, firms , regulators to create
'''
config = {
  "agents": {
    "num_agents": 10,
    "agent_action_space": ['invest'],
    "agent_state_space": ['money'],  # Name of variable
    "reward_function": ["money_agents"],
  },
  "firms": {
    "num_firms": 10,
    "firm_action_space": ['fee_rate'],
    "firm_state_space": ['money'],
    "reward_functions": ["money_firms"],
  },
  "regulators": {
    "num_regulators": 1,  # Leave as 1, there is just 1 gov.
    "reg_action_space": ['fee_rate', 'tax_rate'],
    "tax_rate_agents": 0.10,
    "tax_rate_firms": 0.10,
    "reg_state_space": ['wealth_equality', 'money'],
    "reward_functions": ['money_firms_agents', 'equality_agents']
    # Equality could be measured by the standard deviation of agents (smaller is better). Could make this a negative number
  },
  "general": {
    "save_state_iterations": 1,
    "simulation_run_count": 60,
    "iterations_in_each_simulation_run": 1000
  }
}


def do_centralized_world_interactions(environment, i):
  # Agents interact with each other
  environment.interact_agents_with_agents()

  # Agents interact with firms
  environment.interact_firms_with_agents()

  # Firms interact with firmsooo
  environment.interact_firms_with_firms()

  # Government regulate firms (maybe penalize)
  if i % 52 == 0:
    environment.regulators_regulate_firms()

  # Government regulate individuals
  if i % 52 == 0:
    environment.regulators_regulate_agents()


def do_decentralized_world_interactions(environment, i):
  # Agents decide interest rate and give a cut to Crypto firms 
  environment.decentralized_lending()
  # Government regulate firms (maybe penalize)
  if i % 52 == 0:
    environment.regulators_regulate_firms()

  # Government regulate individuals
  if i % 52 == 0:
    environment.regulators_regulate_agents()

  # Agent-agent interaction (betting)
  environment.interact_agents_with_agents()
  

  #environment.d_interact_agentSeeking_with_firm_with_agentLending()
  #environment.d_interact_regulator_with_agentLending()
  #environment.d_interact_regulator_with_firm()
  #environment.d_interact_agents_with_agents()
  pass


def simulate(config, simulation_run_number, is_centralized):
  environment = Economy(config, is_centralized)
  environment.configure_agents()
  environment.configure_firms()
  environment.configure_regulators()

  num_iterations = config["general"]["iterations_in_each_simulation_run"]
  for i in range(1, num_iterations + 1):
    if is_centralized:
      do_centralized_world_interactions(environment, i)
    else:
      do_decentralized_world_interactions(environment, i)

    # Modulo operator = "remainder operator"
    if (i == 1 or i == num_iterations
        or (i) % config['general']['save_state_iterations'] == 0):
      environment.save_state(i)
    # all iterations done -- now print the state to a csv file for further analysis
  environment.print_state(simulation_run_number)
  return environment.summary

def cleanOutputFolder(mode):
  folder_path = "runoff"
  shutil.rmtree(folder_path)
  os.mkdir(folder_path)



def run(mode):
  cleanOutputFolder(mode)
  if mode == "centralized":
    is_centralized = True
  else:
    is_centralized = False

  summary_of_all_runs = []
  # run simulate N times with M Iterations in each run
  for i in range(config["general"]["simulation_run_count"]):

    summary_data_for_onerun = simulate(config, i, is_centralized)
    summary_of_all_runs.extend(summary_data_for_onerun)

  # print summary of all the runs

  # write summary of all the simulation runs into a csv file
  filename = mode + "_output/summary.csv"
  list = summary_of_all_runs
  #write the header of the csv file
  with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list[0].keys())
    writer.writeheader()

  #write the content of the array to csv file
  with open(filename, 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list[0].keys())
    for row in list:
      writer.writerow(row)


#start the similation
#run("centralized")
run("decentralized")
