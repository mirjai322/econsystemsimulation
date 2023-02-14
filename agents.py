# Agents should each have an action space
# Econs - completely rational consumer'
import uuid

class Agent:

  def __init__(self, config):
    self.id = uuid.uuid1()
    print(self.id)
    self.net_worth = 0
    self.risk_appetite = None
    self.credit_score = None
    self.savings_rate = None
    self.income = None
    self.base_action_space = None


def update_action_space(self, new_action_space):
  self.action_space = new_action_space


# questions:
# how to calculate income/net worth of each agent -- initial
