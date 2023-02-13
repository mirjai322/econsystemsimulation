economy = {
      "money": 1000,
      "houses": 10,
      "cars": 1000,
}

base_economy = {"money": 1000}
import numpy
import sys


class Regulators:
  pass

sum = 0
mean = 0

def find_median():
  pass
def find_mean():
  #list of all net worths = net_worths
  for(i = 0; i<= list.length-1; i++):
    sum = sum + list[i]
  mean = sum/(list.length - 1)
    

class Economy:

  def __init__(
    self,
    economy_config
    # num_agents,
    # action_space, # set of all possible actions 
    # state_space,  # set of all possible states 
    # num_firms,
    # resources=base_economy, #?
    # regulations=None,
  ):
    self.config = economy_config
    self.num_agents = num_agents
    # Fill this out
    self.num_firms = num_firms
    self.action_space = action_space
    self.state_space = state_space

  def configure_agents(self):
    self.agents = []
    for i in range(self.config['agents']['num_agents']):
      self.agents.append(Agent(self.config['agents']))

  def configure_firms(self):
    self.firms = []
    for i in range(self.config['firms']['num_firms']):
      self.agents.append(Firm(self.config['firms']))

  def configure_regulators(self):
    self.regulators = [] # Might just be a list of 1 item
    for i in range(self.config['regulators']['num_regulators']):
      self.agents.append(Firm(self.config['regulators']))

  def interact_agents_with_agents(self):
    agent_win = random.choice(agents)
    agents.remove(agent_win)
    agent_lose =  random.choice(agents)
    agent_win.net_worth = net_worth + agent_lose.net_worth
    agent_lose.net_worth = net_worth
    
"""
    0. Determine number of interactions (could also pair people up)
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
    #reset

    
    # Some code here 
    print("some outputs") 
    sys.exit(1)
    # Inside the function scope

  def interact_firms_with_firms(self):
    """
    create new firm (as a combination with another) and get rid of previous 2 -- aka merger
    set fees equal to current and another firm, take that average? (adjusting fees based on other firm fees)
    """

  def regulators_regulate_firms():
    """
    #median, standard dev and mean income of all agents
    #is fee greater than some percentage of that (ex/ 10 %)
    if fees > maxAmount:
      
    every x iteration, call change_regulations() function

    antitrust: if there is a new firm formed that is the composition, then split that firm back into original
    """

  def regulators_regulate_agents():
    """
    every x iteration, call change_regulations() function
    
    regulator income increases by how much each agent loses (additive)
    """

  def change_regulations():
    """
    "coin flip" -- either increase or decrease tax rate

    run antitrust regulatation or stop it
    """
    

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


    
  


  
