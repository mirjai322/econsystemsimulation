from agents import Agent
from firms import Firm
from regulators import Regulator
from numpy import random
import numpy as np
from ledger import Ledger
import csv


class Economy:

  def __init__(self, config):
    self.config = config
    self.num_agents = config["agents"]["num_agents"]
    self.num_firms = config["firms"]["num_firms"]
    self.num_regulators = config["regulators"]["num_regulators"]
    self.state = []
    self.ledger = Ledger()

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

  def interact_agents_with_agents(self):
    """
        1. Randomly pick two agents (people)
        2. Randomly have each of them bet a percentage of their money based on who they are
        3. Have one of the agents win, and take the money, the other lose and lose money

        Policies:
        If netWorth > 500k:
          Invest 40%
          Bet more often @TODO
        Else:
          Invest 10%
          Bet less often @TODO
    """
    agent_win = random.choice(self.agents)
    agent_lose = random.choice(self.agents)
    #what if agent_lose is same as agent_win @TODO

    if agent_lose.net_worth > 500000:
      bet_amount = 0.4 * agent_lose.net_worth
    else:
      bet_amount = 0.1 * agent_lose.net_worth

    agent_win.net_worth = agent_win.net_worth + bet_amount
    agent_lose.net_worth = agent_lose.net_worth - bet_amount

  def interact_firms_with_agents(self):
    """
    interact_firms_with_agents
    1. Agent borrows random number of money from bank (between 100-10,000) - aka a loan - store value in variable "loan"
    2. Every 5 iterations (or some other number), agent "pays interest"
      1. 10% of "loan" is subtracted from agent's networth
      2. 10% of "loan" is added to bank's networth
    """
    # create a new loan between a randomg agent and random firm 
    firm = random.choice(self.firms)
    agent = random.choice(self.agents)
    loan_amount = random.randint(100, 10000)
    firm.money = firm.money - loan_amount
    agent.net_worth = agent.net_worth + loan_amount
    #print ("loan initiated")
    self.ledger.initiate_loan(agent, firm, loan_amount)

    # scan ledger and randomly pick one loan to default, one loan if any to pay_off, and random interest payment 
    # pay interest on loan 
    if len(self.ledger.entries) > 5:
      entry = random.choice(self.ledger.entries)
      amount = entry.amount
      interest_amount = 0.1*amount
      entry.firm.money += interest_amount
      entry.agent.net_worth -= interest_amount
      #print ("loan interest paid")
      # pay off a random loan 
      entry = random.choice(self.ledger.entries)
      loan_amount = entry.amount
      entry.firm.money += amount 
      entry.agent.net_worth -= amount 
      self.ledger.settle_loan(entry.agent.id,entry.firm.id)
      
      # default on a random loan?? firm loses money, what should happen to agent? reduce credit rating? @TODO
      
    
    

  def interact_firms_with_firms(self):
    """
    create new firm (as a combination with another) and get rid of previous 2 -- aka merger
    set fees equal to current and another firm, take that average? (adjusting fees based on other firm fees)
    """
    pass

  def regulators_regulate_firms(self):
    """
     #median, standard dev and mean income of all agents
     #is fee greater than some percentage of that (ex/ 10 %)
     if fees > maxAmount:

     every x iteration, call change_regulations() function

     antitrust: if there is a new firm formed that is the composition, then split that firm back into original
     """
    pass

  def regulators_regulate_agents(self):
    pass
    """
    every x iteration, call change_regulations() function

    regulator income increases by how much each agent loses (additive)
    """

  def change_regulatpass(self):
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
      data["money"] = "{:.2f}".format(agent.net_worth)
      agent_id = agent_id + 1
      list.append(data)

    firm_id = 0
    for firm in self.firms:
      data = {}
      data["iteration"] = current_iteration_count
      data["type"] = "firm"
      data["id"] = "F" + str(firm_id)
      data["money"] = "{:.2f}".format(firm.money)
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

    # create numpy array
    money_array = np.array([agent.net_worth for agent in self.agents])
    max = np.max(money_array)
    min = np.min(money_array)
    median = np.median(money_array)
    mean = np.mean(money_array)
    stddev = np.std(money_array)

    print ("Agent Stats:")
    print ("Min: " + self.formatNumber(min))
    print ("Max: " + self.formatNumber(max))
    print ("Mean: " + self.formatNumber(mean))
    print ("Median: " + self.formatNumber(median))
    print ("Std Dev: " + self.formatNumber(stddev))
    print ("-------------------------------------------------------")
    print ()

    money_array = np.array([firm.money for firm in self.firms])
    max = np.max(money_array)
    min = np.min(money_array)
    median = np.median(money_array)
    mean = np.mean(money_array)
    stddev = np.std(money_array)

    print ("Firm Stats:")
    print ("Min: " + self.formatNumber(min))
    print ("Max: " + self.formatNumber(max))
    print ("Mean: " + self.formatNumber(mean))
    print ("Median: " + self.formatNumber(median))
    print ("Std Dev: " + self.formatNumber(stddev))
    print ("-------------------------------------------------------")
    print ()


  def formatNumber(self,num):
    return str("{:.2f}".format(num))

