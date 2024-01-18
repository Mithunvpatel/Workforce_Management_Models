class CallCenterModel:
    def __init__(self, call_volume, service_level_goal, avg_handling_time, shrinkage, agent_productivity, overflow_agreement):
        self.call_volume = call_volume
        self.service_level_goal = service_level_goal
        self.avg_handling_time = avg_handling_time
        self.shrinkage = shrinkage
        self.agent_productivity = agent_productivity
        self.overflow_agreement = overflow_agreement

    def calculate_fte_requirements(self):
        # Calculate the number of calls that need to be handled within the service level goal
        calls_within_service_level = self.call_volume * self.service_level_goal

        # Adjust for shrinkage
        calls_after_shrinkage = calls_within_service_level / (1 - self.shrinkage)

        # Calculate the total handle time required in hours
        total_handle_time_hours = calls_after_shrinkage * self.avg_handling_time / 3600

        # Calculate the FTE requirements
        fte_requirements = total_handle_time_hours / self.agent_productivity

        # Adjust for overflow agreement
        fte_requirements *= self.overflow_agreement

        return fte_requirements


# Example usage with adjustable variables
call_volume = 50000  # Adjust based on your expected call volume
service_level_goal = 0.7  # Adjust based on your service level goals
avg_handling_time = 300  # Average handling time in seconds
shrinkage = 0.15  # Adjust based on your shrinkage rate
agent_productivity = 0.75  # Adjust based on your agent productivity
overflow_agreement = 1.2  # Adjust based on your overflow agreement terms

# Create an instance of the CallCenterModel
model = CallCenterModel(call_volume, service_level_goal, avg_handling_time, shrinkage, agent_productivity, overflow_agreement)

# Calculate FTE requirements
fte_requirements = model.calculate_fte_requirements()

# Display the results
print(f"FTE Requirements: {fte_requirements:.2f}")