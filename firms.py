# Service fees here
# Regulated by the government (or the people) and service the people

#Firm Actions
##*controls flow of money
###* loan money (w/ interest rate)
###* can prevent you from borrowing money if your credit score is below a certain number
###* store deposited money (w/ interest rate)
###* can print more money
###* general service fees
###* “waiting time” when liquidating
import uuid


class Firm:

  def __init__(self, config):
    self.money = None
    self.id = uuid.uuid1()

  def service_fees():
    pass


class DecentralizedFirm:

  def __init__(self, service_fees):
    # Maybe some people don't want to be depositors etc.
    # self.active_agents = all_agents
    self.id = uuid.uuid1()

  def service_fees():
    pass
