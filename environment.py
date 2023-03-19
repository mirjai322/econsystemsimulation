from agents import Agent
from firms import Firm
from regulators import Regulator
from numpy import random
import numpy as np
from ledger import Ledger
import csv


class Economy:

  def __init__(self, config, is_centralized):
    self.config = config
    self.num_agents = config["agents"]["num_agents"]
    self.num_firms = config["firms"]["num_firms"]
    self.num_regulators = config["regulators"]["num_regulators"]
    self.state = []
    self.summary = []
    self.ledger = Ledger()
    self.is_centralized = is_centralized

  def configure_agents(self):
    self.agents = []
    for i in range(self.config['agents']['num_agents']):
      a = Agent(self.config['agents'])
      #choose two random number between 1 and 100 and then multiply them by 10000 to assign random networth
      rand_num = random.randint(1, 101)
      rand_num2 = random.randint(1, 101)
      a.net_worth = rand_num * rand_num2 * 10000
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
      r = Regulator(self.config['regulators'])
      rand_num = random.randint(1, 101)
      r.income = rand_num * 10000000
      self.regulators.append(r)
      #self.regulators.append(Regulator(self.config['regulators']))

  # ALL decentralized interactions below
  def decentralized_lending(self):
    '''
    Pick a random agent to be the Seeking Agent
    Pick a random agent to be the Lending Agent
    Pick a random interest rate between 1 -> 20% of the Loan Amount
    Pick a random Firm to be the crypto_lending_firm
    Pick a random transaction fee that is between 1 -> 2% of the Loan Amount
    Loan amount gets added to Seeking Agent net worth
    Transaction Fee amount gets subtracted from Seeking Agent's net worth AND added to crypto_lending_firm money
    Interest Rate gets subtracted from Seeking Agent's net worth AND added to Lending Agent net worth
     '''

    seeking_agent = random.choice(self.agents)
    lending_agent = None
    exclude = seeking_agent
    #make sure seeking_agent != lending_agent
    while lending_agent == None or lending_agent == exclude:
      lending_agent = random.choice(self.agents)
    upperBound = np.minimum(0.4 * seeking_agent.net_worth,
                            0.2 * lending_agent.net_worth)
    if upperBound <= 100:
      return
    #setting loan amount
    loan_amount = np.random.randint(90, upperBound)

    #choosing firm that is like blockchain network "provider" - ex/ Ethereum chain
    crypto_lending_firm = random.choice(self.firms)
    #setting transaction fee
    min_transaction_fee = 0.15 * loan_amount
    max_transaction_fee = 0.20 * loan_amount
    transaction_fee = np.random.uniform(min_transaction_fee,
                                        max_transaction_fee)
    crypto_lending_firm.money += transaction_fee
    seeking_agent.net_worth -= transaction_fee
    #give agent loan money
    seeking_agent.net_worth += loan_amount
    #every iteration, you keep paying the percentage of the loan (interest_rate * loan_amount) back to the lending agent, until the entire loan is paid off
    #seeking_agent.net_worth -= interest_rate
    #lending_agent.net_worth += interest_rate
    self.ledger.initiate_loan(seeking_agent, crypto_lending_firm, loan_amount,
                              lending_agent)

    # scan ledger and randomly pick one loan if any to pay_off, and make interest payment
    # pay interest on loan
    if len(self.ledger.entries) > 5:
      entry = random.choice(self.ledger.entries)
      amount = entry.amount
      #setting interest rate
      min_interest = 0.22 * amount
      max_interest = 0.28 * amount
      interest = np.random.uniform(min_interest, max_interest)
      entry.lending_agent.net_worth += interest
      entry.agent.net_worth -= interest
      #print("loan interest paid" + str(interest))
      # pay off a random loan
      entry = random.choice(self.ledger.entries)
      loan_amount = entry.amount
      entry.firm.money += amount
      entry.agent.net_worth -= amount
      self.ledger.settle_loan_between_agent_and_agent(entry.agent.id,
                                                      entry.lending_agent.id)

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

    #if agent_lose net worth is less than 100 OR if agent_win net worth - agent_lose net worth absolute value is greater than 10000
    if agent_lose.net_worth < 100 or agent_win.net_worth < 100 or np.abs(
        agent_win.net_worth - agent_lose.net_worth) > 10000:
      agent_win = random.choice(self.agents)
      agent_lose = random.choice(self.agents)

    if agent_lose.net_worth > 500000:
      bet_amount = 0.4 * agent_lose.net_worth
    else:
      bet_amount = 0.1 * agent_lose.net_worth

    agent_win.net_worth = agent_win.net_worth + bet_amount
    agent_lose.net_worth = agent_lose.net_worth - bet_amount
    #transaction fee logic to incorporate firms in transactions
    transaction_fee_percentage = np.random.uniform(0.15, 0.20)
    transaction_fee = bet_amount * transaction_fee_percentage
    #choose random firm, that is the firm that facilitated the transaction
    handler = random.choice(self.firms)
    handler.money += transaction_fee
    agent_win.net_worth -= transaction_fee / 2
    agent_lose.net_worth -= transaction_fee / 2

  def interact_firms_with_agents(self):
    """
    interact_firms_with_agents
    1. Agent borrows random number of money from bank (between 100-10,000) - aka a loan - store value in variable 
    "loan"
    2. Every 5 iterations (or some other number), agent "pays interest"
      1. 10% of "loan" is subtracted from agent's networth
      2. 10% of "loan" is added to bank's networth
      Every iteration, 10% is paid off -- but if agent's networth hits 0 before loan is paid off, then that is  defaulting: agent is not allowed to take out more loans
    Bank will not give a loan that exceeds 50 percent of agent's networth AND/OR bank cannot give a loan that exceeds 10% of its net worth
    """
    # create a new loan between a random agent and random firm
    # select a random firm whose total money >= 100
    # if the firm has less than 100 dollars, then skip the loan and make that firm bankrupt and remove it from the list.
    # the actual logic of what should happen to outstanding loans when your bankrupt a firm -- like sell the loans to other firms??
    # for now ..we will just skip the loan

    # Weighted random selection
    firm_weights_raw = np.array([firm.money for firm in self.firms])
    if firm_weights_raw.sum() <= 0 or np.any(firm_weights_raw < 0):
      return  # Return or handle the case where the sum of firm weights is zero or negative or there are negative weights.

    firm_weights = firm_weights_raw / firm_weights_raw.sum()
    if not np.isclose(firm_weights.sum(), 1):
      # Handle the case where the probabilities do not sum up to 1.
      # One option is to renormalize the probabilities:
      firm_weights /= firm_weights.sum()

    agent_firm_choice_index = np.random.choice(range(firm_weights.shape[0]),
                                               p=firm_weights)
    selected_firm = self.firms[agent_firm_choice_index]

    #Fully random selection
    #firm = random.choice(self.firms)
    #if firm.money <= 100:
    #return
    agent = random.choice(self.agents)
    #specify valid loan amount
    upperBound = np.minimum(0.70 * agent.net_worth, 0.3 * selected_firm.money)
    if upperBound <= 100:
      return
    loan_amount = np.random.randint(90, np.maximum(upperBound, 100))

    selected_firm.money = selected_firm.money - loan_amount
    agent.net_worth = agent.net_worth + loan_amount
    #print ("loan initiated")
    self.ledger.initiate_loan(agent, selected_firm, loan_amount)

    # scan ledger and randomly pick one loan to default, one loan if any to pay_off, and random interest payment
    # pay interest on loan
    if len(self.ledger.entries) > 5:
      entry = random.choice(self.ledger.entries)
      amount = entry.amount
      interest_amount = 0.10 * amount
      entry.firm.money += interest_amount
      entry.agent.net_worth -= interest_amount
      #print ("loan interest paid")
      # pay off a random loan
      entry = random.choice(self.ledger.entries)
      loan_amount = entry.amount
      entry.firm.money += amount
      entry.agent.net_worth -= amount
      self.ledger.settle_loan_between_agent_and_firm(entry.agent.id,
                                                     entry.firm.id)

      # default on a random loan?? firm loses money, what should happen to agent? reduce credit rating? @TODO

  def interact_firms_with_firms(self):
    """
    create new firm (as a combination with another) and get rid of previous 2 -- aka merger
    set fees equal to current and another firm, take that average? (adjusting fees based on other firm fees)
    """

    #mergers and spinoffs
    choice = random.choice([0, 1])
    if choice == 1 and len(self.firms) > 5:
      #merger
      firm1 = random.choice(self.firms)
      money1 = firm1.money
      self.firms.remove(firm1)
      firm2 = random.choice(self.firms)
      money2 = firm2.money
      #antitrust regulations -- can be commented out when not applicable
      '''
      Create variable called "firm_sum"
      Iterate through all the firms
      Add the net worth of each firm to the firm_sum
      Create variable called comparison
        Comparison is what percentage of the aggregate shall the potential merger not exceed
      If the potential merger combined net worth exceeds comparison, merger is not carried out (strict regulation).
      But for laissez faire this entire block of code will not matter.
      '''
      
      firm_sum = 0
      for firm in self.firms:
        firm_sum += firm.money
      comparison = 0.65 * firm_sum
      if (money1 + money2) >= comparison:
        #choose 2 different firms
        firm1 = random.choice(self.firms)
        money1 = firm1.money
        self.firms.remove(firm1)
        firm2 = random.choice(self.firms)
        money2 = firm2.money
      
      newFirm = Firm(self.config['firms'])
      newFirm.money = money1 + money2
      self.firms.append(newFirm)
      self.firms.remove(firm2)
    if choice == 0:
      #spinoff
      preSplit = random.choice(self.firms)
      moneyBefore = preSplit.money
      self.firms.remove(preSplit)
      firm1 = Firm(self.config['firms'])
      firm2 = Firm(self.config['firms'])
      firm1.money = moneyBefore / 2
      firm2.money = moneyBefore / 2
      self.firms.append(firm1)
      self.firms.append(firm2)

  def regulators_regulate_firms(self):
    """
     #median, standard dev and mean income of all agents
     #is fee greater than some percentage of that (ex/ 10 %)
     if fees > maxAmount:

     every x iteration, call change_regulations() function

     antitrust: if there is a new firm formed that is the composition, then split that firm back into original
     """
    for item in self.firms:
      money_array = np.array([firm.money for firm in self.firms])
      mean = np.mean(money_array)
      taxRate = 0.0
      if item.money >= mean:
        taxRate = 0.0
      tax_amount = taxRate * item.money
      reg = random.choice(self.regulators)
      reg.income += tax_amount
      item.money -= tax_amount

  def regulators_regulate_agents(self):
    """
    every x iteration, call change_regulations() function

    regulator income increases by how much each agent loses (additive)

    1. iterate through all the agents
      1. if agent's income is less than mean, tax rate = 15%
      2. if agent's income is greater than mean, tax rate = 25%
    """
    for item in self.agents:
    #test tax bracket
      money_array = np.array([agent.net_worth for agent in self.agents])
      mean = np.mean(money_array)
      taxRate = 0.0
      if item.net_worth >= mean:
        taxRate = 0.0
      tax_amount = taxRate * item.net_worth
      item.net_worth = item.net_worth - tax_amount
      reg = random.choice(self.regulators)
      reg.income += tax_amount


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

  def print_state(self, run_number):
    if self.is_centralized:
      prefix = "centralized"
    else:
      prefix = "decentralized"
    #filename = prefix + "runoff/detail_data_iteration_" + str(run_number) + ".csv"
    filename = "runoff/detail_data_iteration" + str(run_number) + ".csv"
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

    summary_data = {}
    summary_data["run"] = run_number
    summary_data["type"] = "agent"
    # create numpy array
    money_array = np.array([agent.net_worth for agent in self.agents])
    max = np.max(money_array)
    summary_data["max"] = max

    min = np.min(money_array)
    summary_data["min"] = min

    median = np.median(money_array)
    summary_data["median"] = median

    mean = np.mean(money_array)
    summary_data["mean"] = mean

    stddev = np.std(money_array)
    summary_data["stddev"] = stddev

    self.summary.append(summary_data)

    print("Agent Stats:")
    print("Min: " + self.formatNumber(min))
    print("Max: " + self.formatNumber(max))
    print("Mean: " + self.formatNumber(mean))
    print("Median: " + self.formatNumber(median))
    print("Std Dev: " + self.formatNumber(stddev))
    print("-------------------------------------------------------")
    print()

    # summary of firms
    summary_data = {}
    summary_data["run"] = run_number
    summary_data["type"] = "firm"

    money_array = np.array([firm.money for firm in self.firms])
    max = np.max(money_array)
    summary_data["max"] = max

    min = np.min(money_array)
    summary_data["min"] = min

    median = np.median(money_array)
    summary_data["median"] = median

    mean = np.mean(money_array)
    summary_data["mean"] = mean

    stddev = np.std(money_array)
    summary_data["stddev"] = stddev

    self.summary.append(summary_data)

    print("Firm Stats:")
    print("Min: " + self.formatNumber(min))
    print("Max: " + self.formatNumber(max))
    print("Mean: " + self.formatNumber(mean))
    print("Median: " + self.formatNumber(median))
    print("Std Dev: " + self.formatNumber(stddev))
    print("# of Firms:" + str(len(self.firms)))
    print("-------------------------------------------------------")
    print()

    #reset the state to None for the next iteration
    self.state = None

  def formatNumber(self, num):
    return str("{:.2f}".format(num))
