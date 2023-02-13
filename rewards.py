import numpy as np


def reg_money_firms_agents(reg, agents, firms):
    # Goal: return the total money that the government gets in taxes
    # "tax_rate_agents": 0.10,
    # "tax_rate_firms": 0.20,
    # for agents
    wealth_agent = np.array([agent.money for agent in agents])
    money_reg_agent = reg.tax_rate_agents * wealth_agent
    wealth_firm = np.array([firm.money for firm in firms])
    money_reg_firm = reg.tax_rate_firms * wealth_firm
    return (money_reg_agent + money_reg_firm)


def equality_agents(agents):
    # Input: list of all of your agents
    # 1. collect all the "wealth" values from each agent
    # 2. Get standard deviation of this list (stdev > 0)
    # find standard deviation of list, store in variable
    wealth = np.array([agent.money for agent in agents])
    wealth_std = wealth.std()
    return -wealth_std  # Intuition: large std = inequality = low number


def money_agents(
        agent1_bet, agent2_bet,
        agent1_win_prob, agent2_win_prob,
):
    agent1_norm_bet_prob = (agent1_win_prob /
                            (agent1_win_prob + agent2_win_prob)
                            )
    bet = np.random.rand()  # Random number between zero and 1
    prize = agent1_bet + agent2_bet
    agent1_win = bet < agent1_norm_bet_prob
    return {
        "agent1": prize if agent1_win else 0,
        "agent2": 0 if agent1_win else prize
    }


def get_raise(agent, transaction):
    pass


def investment_payout(agent, transaction):
    pass


def bankruptcy(agent, transaction):
    pass
    # Update the agent somehow with a number


def gov_aid(agent, transaction):  # some sort of governmental aid (ex/ stimulus check)
    pass
