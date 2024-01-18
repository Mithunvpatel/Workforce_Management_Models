
import pandas as pd

class MonthlyCallCenterModel:
    def __init__(self, monthly_call_volumes, service_level_goal, avg_handling_time, shrinkage, agent_productivity, overflow_agreement):
        self.monthly_call_volumes = monthly_call_volumes
        self.service_level_goal = service_level_goal
        self.avg_handling_time = avg_handling_time
        self.shrinkage = shrinkage
        self.agent_productivity = agent_productivity
        self.overflow_agreement = overflow_agreement

    def calculate_monthly_fte_requirements(self):
        monthly_fte_requirements = []

        for call_volume in self.monthly_call_volumes:
            # Calculate the number of calls that need to be handled within the service level goal
            calls_within_service_level = call_volume * self.service_level_goal

            # Adjust for shrinkage
            calls_after_shrinkage = calls_within_service_level / (1 - self.shrinkage)

            # Calculate the total handle time required in hours
            total_handle_time_hours = calls_after_shrinkage * self.avg_handling_time / 3600

            # Calculate the FTE requirements
            fte_requirements = total_handle_time_hours / self.agent_productivity

            # Adjust for overflow agreement
            fte_requirements *= self.overflow_agreement

            monthly_fte_requirements.append(fte_requirements)

        return monthly_fte_requirements


# Example usage with adjustable monthly variables
monthly_call_volumes = [50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000, 105000]
service_level_goal = 0.8  # Adjust based on your service level goals
avg_handling_time = 180  # Average handling time in seconds
shrinkage = 0.15  # Adjust based on your shrinkage rate
agent_productivity = 0.75  # Adjust based on your agent productivity
overflow_agreement = 1.2  # Adjust based on your overflow agreement terms

# Create an instance of the MonthlyCallCenterModel
monthly_model = MonthlyCallCenterModel(monthly_call_volumes, service_level_goal, avg_handling_time, shrinkage, agent_productivity, overflow_agreement)

# Define month names
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Calculate monthly FTE requirements
monthly_fte_requirements = monthly_model.calculate_monthly_fte_requirements()

# Display the results with month names, monthly call volumes, and average handling times
for month, call_volume, avg_handling_time, fte_requirements in zip(month_names, monthly_call_volumes, [avg_handling_time]*len(month_names), monthly_fte_requirements):
    print(f"{month}: Call Volume - {call_volume}, Avg Handling Time - {avg_handling_time} seconds, FTE Requirements - {fte_requirements:.2f}")

# Create a dictionary with the data
data = {
    'Month': month_names,
    'Call Volume': monthly_call_volumes,
    'Avg Handling Time': avg_handling_time,
    'FTE Requirements': monthly_fte_requirements,
    'service level goal': service_level_goal
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)