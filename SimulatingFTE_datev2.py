import pandas as pd

class MonthlyCallCenterModel:
    def __init__(self, monthly_call_volumes, service_level_goals, avg_handling_times, shrinkages, agent_productivities, overflow_agreements):
        self.monthly_call_volumes = monthly_call_volumes
        self.service_level_goals = service_level_goals
        self.avg_handling_times = avg_handling_times
        self.shrinkages = shrinkages
        self.agent_productivities = agent_productivities
        self.overflow_agreements = overflow_agreements

    def calculate_monthly_fte_requirements(self):
        monthly_fte_requirements = []

        for call_volume, service_level_goal, avg_handling_time, shrinkage, agent_productivity, overflow_agreement in zip(
                self.monthly_call_volumes, self.service_level_goals, self.avg_handling_times,
                self.shrinkages, self.agent_productivities, self.overflow_agreements):
            # Calculate the number of calls that need to be handled within the service level goal
            calls_within_service_level = call_volume * service_level_goal

            # Adjust for shrinkage
            calls_after_shrinkage = calls_within_service_level / (1 - shrinkage)

            # Calculate the total handle time required in hours
            total_handle_time_hours = calls_after_shrinkage * avg_handling_time / 3600

            # Calculate the FTE requirements
            fte_requirements = total_handle_time_hours / agent_productivity

            # Adjust for overflow agreement
            fte_requirements *= overflow_agreement

            monthly_fte_requirements.append(fte_requirements)

        return monthly_fte_requirements

# Example usage with adjustable monthly variables as lists
monthly_call_volumes = [50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000, 105000]
service_level_goals = [0.8, 0.85, 0.85, 0.9, 0.9, 0.85, 0.8, 0.8, 0.85, 0.9, 0.95, 0.95]
avg_handling_times = [180, 175, 170, 165, 160, 160, 165, 170, 175, 180, 185, 190]
shrinkages = [0.15, 0.14, 0.14, 0.13, 0.13, 0.14, 0.15, 0.15, 0.14, 0.13, 0.12, 0.12]
agent_productivities = [0.75, 0.76, 0.77, 0.78, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72]
overflow_agreements_1 = [1.2, 1.2, 1.1, 1.1, 1.2, 1.3, 1.3, 1.2, 1.2, 1.1, 1.1, 1.2]
overflow_agreements_2 = [1.1, 1.1, 1.2, 1.2, 1.1, 1.0, 1.0, 1.1, 1.1, 1.2, 1.2, 1.1]

# Create an instance of the MonthlyCallCenterModel for each overflow option
monthly_model_1 = MonthlyCallCenterModel(monthly_call_volumes, service_level_goals, avg_handling_times,
                                          shrinkages, agent_productivities, overflow_agreements_1)
monthly_model_2 = MonthlyCallCenterModel(monthly_call_volumes, service_level_goals, avg_handling_times,
                                          shrinkages, agent_productivities, overflow_agreements_2)

# Define month names
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Calculate monthly FTE requirements for each overflow option
monthly_fte_requirements_1 = monthly_model_1.calculate_monthly_fte_requirements()
monthly_fte_requirements_2 = monthly_model_2.calculate_monthly_fte_requirements()

# Create DataFrames for each overflow option
df_1 = pd.DataFrame({
    'Month': month_names,
    'Call Volume': monthly_call_volumes,
    'Avg Handling Time': avg_handling_times,
    'FTE Requirements': monthly_fte_requirements_1,
    'Overflow Agreement': overflow_agreements_1
})

df_2 = pd.DataFrame({
    'Month': month_names,
    'Call Volume': monthly_call_volumes,
    'Avg Handling Time': avg_handling_times,
    'FTE Requirements': monthly_fte_requirements_2,
    'Overflow Agreement': overflow_agreements_2
})

# Display the DataFrames
print("Overflow Option 1:")
print(df_1)

print("\nOverflow Option 2:")
print(df_2)
