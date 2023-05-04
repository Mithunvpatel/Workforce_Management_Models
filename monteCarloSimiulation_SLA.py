import random
import numpy as np
import matplotlib.pyplot as plt

# Define the function that represents your service level logic.
def calculate_service_level(avg_time, std_dev_time, target_time):
    # Simulate service time using a normal distribution.
    service_time = random.normalvariate(avg_time, std_dev_time)
    # If service time is less than or equal to target time, return 1 to represent success.
    if service_time <= target_time:
        return 1
    # Otherwise, return 0 to represent failure.
    else:
        return 0

# Define the parameters for your simulation.
num_simulations = 10000  # Number of times to simulate the service level.
avg_service_time = 3  # Average service time in minutes.
std_dev_service_time = 0.5  # Standard deviation of service time in minutes.
target_service_time = 3.4  # Target service time in minutes.

# Run the simulation.
successes = []
for i in range(num_simulations):
    successes.append(calculate_service_level(avg_service_time, std_dev_service_time, target_service_time))

# Calculate the success rate.
success_rate = sum(successes) / num_simulations

# Calculate the mean and standard deviation of the simulated service times.
service_times = [random.normalvariate(avg_service_time, std_dev_service_time) for i in range(num_simulations)]
mean_service_time = np.mean(service_times)
std_dev_service_time = np.std(service_times)

# Plot the distribution of service times and the target service time.
plt.hist(service_times, bins=50, alpha=0.5, color='blue')
plt.axvline(target_service_time, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Service Time (Minutes)')
plt.ylabel('Count')
plt.title('Distribution of Service Times')
plt.text(8, 800, f"Target Service Time: {target_service_time} min")
plt.text(8, 750, f"Success Rate: {success_rate:.2%}")
plt.text(8, 700, f"Mean Service Time: {mean_service_time:.2f} min")
plt.text(8, 650, f"Standard Deviation: {std_dev_service_time:.2f} min")
plt.show()
