import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

############################################################################
#Figure 1: Pick a random run and show how agent networth changes per week
############################################################################

figure, subplot = plt.subplots(nrows=2, ncols=3, figsize=(12, 8), sharey=True)

# Plot something in each subplot
filename = "centralized_low_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration",
             y="money",
             hue="type",
             data=df_agent,
             ax=subplot[0, 0]) #group based on type (agent, firm)
subplot[0, 0].set_title('[Centralized-Low]')

filename = "centralized_medium_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration",
             y="money",
             hue="id",
             data=df_agent,
             ax=subplot[0, 1])
subplot[0, 1].set_title('[Centralized-Medium]')

filename = "centralized_high_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration",
             y="money",
             hue="id",
             data=df_agent,
             ax=subplot[0, 2])
subplot[0, 2].set_title('[Centralized-High]')

filename = "decentralized_low_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration",
             y="money",
             hue="id",
             data=df_agent,
             ax=subplot[1, 0])
subplot[1, 0].set_title('[Decentralized-Low]')

filename = "decentralized_medium_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df.round(2)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration",
             y="money",
             hue="id",
             data=df_agent,
             ax=subplot[1, 1])
subplot[1, 1].set_title('[Deentralized-Medium]')

filename = "decentralized_high_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration",
             y="money",
             hue="id",
             data=df_agent,
             ax=subplot[1, 2])
subplot[1, 2].set_title('[Decentralized-High]')

# Add a main title for the entire figure
figure.suptitle("Agents networth changes in a particular run")

############################################################################
# Figure 2: stddev under different runs
############################################################################

figure, subplot = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

# Plot something in each subplot
filename = "centralized_low_output/summary.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
subplot[0, 0].plot(df_agent['run'], df_agent['stddev'])
subplot[0, 0].set_title('[Centralized-Low]')

filename = "centralized_medium_output/summary.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
subplot[0, 1].plot(df_agent['run'], df_agent['stddev'])
subplot[0, 1].set_title('[Centralized-Medium]')

filename = "centralized_high_output/summary.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
subplot[0, 2].plot(df_agent['run'], df_agent['stddev'])
subplot[0, 2].set_title('[Centralized-High]')

filename = "decentralized_low_output/summary.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
subplot[1, 0].plot(df_agent['run'], df_agent['stddev'])
subplot[1, 0].set_title('[Decentralized-Low]')

filename = "decentralized_medium_output/summary.csv"
df = pd.read_csv(filename)
df.round(2)
df_agent = df[df["type"] == "agent"]
subplot[1, 1].plot(df_agent['run'], df_agent['stddev'])
subplot[1, 1].set_title('[Deentralized-Medium]')

filename = "decentralized_high_output/summary.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
subplot[1, 2].plot(df_agent['run'], df_agent['stddev'])
subplot[1, 2].set_title('[Decentralized-High]')

# Add a main title for the entire figure
figure.suptitle('Standard Deviation of Agent Networth')
"""
############################################################################
# Figure 3: how did poor , middle and rich do at the end?
# group agents into poor, middle and rich
# plot number of poors, middle and rich at every 100 weeks or at start and then at end?
# 3 bar charts at beginning , end and may be after every 100
############################################################################

figure, subplot = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

# Plot something in each subplot
filename = "centralized_low_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration", y="money", hue="id", data=df_agent, ax=subplot[0,0])
subplot[0, 0].set_title('[Centralized-Low]')


filename = "centralized_medium_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration", y="money", hue="id", data=df_agent, ax=subplot[0,1])
subplot[0, 1].set_title('[Centralized-Medium]')

filename = "centralized_high_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration", y="money", hue="id", data=df_agent, ax=subplot[0,2])
subplot[0, 2].set_title('[Centralized-High]')

filename = "decentralized_low_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration", y="money", hue="id", data=df_agent, ax=subplot[1,0])
subplot[1, 0].set_title('[Decentralized-Low]')

filename = "decentralized_medium_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df.round(2)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration", y="money", hue="id", data=df_agent, ax=subplot[1,1])
subplot[1, 1].set_title('[Deentralized-Medium]')

filename = "decentralized_high_output/detail_data_iteration37.csv"
df = pd.read_csv(filename)
df_agent = df[df["type"] == "agent"]
sns.lineplot(x="iteration", y="money", hue="id", data=df_agent, ax=subplot[1,2])
subplot[1, 2].set_title('[Decentralized-High]')

# Add a main title for the entire figure
figure.suptitle("Agents networth changes in a particular run")




"""
plt.show()
