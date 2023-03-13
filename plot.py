import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file as a Pandas DataFrame
df = pd.read_csv('centralized_output/detail_data_iteration_0.csv')

# Filter the DataFrame to only include rows where ID is equal to 'G0'
g0_df = df[df['id'] == 'G0']

# Group the data by iteration and plot each group with a different color
grouped = g0_df.groupby('iteration')
for i, group in grouped:
    plt.plot(group['iteration'], group['money'], label=f'Iteration {i}', color=f'C{i}')

# Add labels, title, and legend to the plot
plt.xlabel('Step')
plt.ylabel('Money')
plt.title('G0 Money over 10 Iterations')
plt.legend()
plt.show()