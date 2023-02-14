class LedgerEntry:
  def __init__(self):
    pass




class Ledger:

  def __init__(self):
    self.entries = []
    pass

  def initiate_loan(self, agent, firm, amount ):
    """
    To create a loan, create an entry in the ledger with the agent reference, firm reference and the amount
    """
    entry = LedgerEntry()
    entry.agent = agent
    entry.firm = firm
    entry.amount = amount
    self.entries.append(entry)
    

  def settle_loan(self, agent_id, firm_id):
    """
    to settle loan, i.e delete the loan form the ledger, pass the agent_id and firm_id
    """
    i = 0
    for entry in self.entries:
      if entry.agent.id== agent_id and entry.firm.id == firm_id:
        self.entries.pop(i)
        #print ("deleted"+ str(i))
        break
      i = i+1


      

        
