import pandas as pd

# Define the input parameters
hours = [f"{i}:00 - {i+1}:00" for i in range(24)]  # intervals
sla = [0.8] * 24  # service level agreement
staff = [30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 55, 55, 60, 60, 65, 65, 70, 70, 75, 75, 80, 80, 85, 85]  # number of agents per interval
aht = [180] * 24  # average handle time (in seconds)
transactions = [200, 220, 250, 270, 300, 330, 360, 400, 450, 500, 550, 600, 650, 700, 750, 800,
                850, 900, 950, 1000, 1050, 1100, 1150, 1200]  # number of transactions per interval

# Create the data table
data = {
    'Intervals': hours,
    'SLA': sla,
    'Staff': staff,
    'AHT': aht,
    'Transactions': transactions
}
df = pd.DataFrame(data)

# Print the data table
print(df.to_string(index=False))