from agents import Agent
from firms import Firm
from regulators import Regulator
from numpy import random
import csv


class Economy:

  def __init__(self, config):
    self.config = config
    self.num_agents = config["agents"]["num_agents"]
    self.num_firms = config["firms"]["num_firms"]
    self.num_regulators = config["regulators"]["num_regulators"]
    self.state = []

  def configure_agents(self):
    self.agents = []
    for i in range(self.config['agents']['num_agents']):
      a = Agent(self.config['agents'])
      #choose two random number between 1 and 100 and then multiply them by 100 to assign random networth
      rand_num = random.randint(1, 101)
      rand_num2 = random.randint(1, 101)
      a.net_worth = rand_num * rand_num2 * 100
      self.agents.append(a)

  def configure_firms(self):
    self.firms = []
    for i in range(self.config['firms']['num_firms']):
      f = Firm(self.config['firms'])
      rand_num = random.randint(1, 101)
      f.money = rand_num * 1000000
      self.firms.append(f)
      # assign random networth between 1B to 100B

  def configure_regulators(self):
    self.regulators = []  # Might just be a list of 1 item
    for i in range(self.config['regulators']['num_regulators']):
      self.regulators.append(Regulator(self.config['regulators']))

  """
        1. Randomly pick two agents (people)
        2. Randomly have each of them bet a percentage of their money based on who they are
        3. Have one of the agents win, and take the money, the other lose and lose money

        Policies:
        If netWorth > 500k:
          Invest 40%
          Bet more often
        Else:
          Invest 10%
          Bet less often
    """

  def interact_agents_with_agents(self):
    agent_win = random.choice(self.agents)
    agent_lose = random.choice(self.agents)
    #what if agent_lose is same as agent_win

    if agent_lose.net_worth > 500000:
      bet_amount = 0.4 * agent_lose.net_worth
    else:
      bet_amount = 0.1 * agent_lose.net_worth

    agent_win.net_worth = agent_win.net_worth + bet_amount
    agent_lose.net_worth = agent_lose.net_worth - bet_amount

  def interact_firms_with_agents(self):
    pass

  """
    create new firm (as a combination with another) and get rid of previous 2 -- aka merger
    set fees equal to current and another firm, take that average? (adjusting fees based on other firm fees)
    """

  def interact_firms_with_firms(self):
    pass

  """
     #median, standard dev and mean income of all agents
     #is fee greater than some percentage of that (ex/ 10 %)
     if fees > maxAmount:

     every x iteration, call change_regulations() function

     antitrust: if there is a new firm formed that is the composition, then split that firm back into original
     """

  def regulators_regulate_firms(self):
    pass

  def regulators_regulate_agents(self):
    pass

  """
    every x iteration, call change_regulations() function

    regulator income increases by how much each agent loses (additive)
    """

  def change_regulations(self):
    pass

  """
    "coin flip" -- either increase or decrease tax rate

    run antitrust regulatation or stop it


    # def two_agents_transact(self,
    #   agent1, agent2, transaction):
    #   pass
    
    # def agents_transact(self, agents, transaction):
    #   pass
    
    # def _regulate_agent(self):
    #   pass
    
    # def _regulate_firm(self):
    #   pass
    
    # def _condition_action_space(agent):
    #   new_actions = None
    #   agent.update_action_space(new_actions)
    
    # def regulate(self):
    #   for agent in self.agents:
    #     self._regulate_agent(agent)
    #   for firm in self.firms:
    #     self._regulate_firm(firm)
    
    """

  def save_state(self, current_iteration_count):
    # iterate over all agents and firms and create a simple data structure that can be printed as a csv
    list = self.state
    agent_id = 0
    for agent in self.agents:
      data = {}
      data["iteration"] = current_iteration_count
      data["type"] = "agent"
      data["id"] = "G" + str(agent_id)
      data["money"] = agent.net_worth
      agent_id = agent_id + 1
      list.append(data)

    firm_id = 0
    for firm in self.firms:
      data = {}
      data["iteration"] = current_iteration_count
      data["type"] = "firm"
      data["id"] = "F" + str(firm_id)
      data["money"] = firm.money
      firm_id = firm_id + 1
      list.append(data)

  def print_state(self):
    filename = "output.csv"
    list = self.state

    #write the header of the csv file
    with open(filename, 'w', newline='') as f:
      writer = csv.DictWriter(f, fieldnames=list[0].keys())
      writer.writeheader()

    #write the content of the array to csv file
    with open(filename, 'a', newline='') as f:
      writer = csv.DictWriter(f, fieldnames=list[0].keys())
      for row in list:
        writer.writerow(row)
