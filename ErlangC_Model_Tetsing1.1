import math

def erlangC(A, m, SLA, AHT, staff):
    rho = sum(A) / (sum(staff) * AHT)
    if rho >= 1:
        raise ValueError("Traffic intensity (rho) cannot exceed 1")
    N = math.ceil(A[0] / (staff[0] * (1 - T)))
    for i in range(1, len(A)):
        N = math.ceil(A[i] / (staff[i] * (1 - rho)**N))
    prob_wait = rho**N / (math.factorial(N) * (sum([(rho**n) / math.factorial(n) for n in range(N)]) + (rho**N / (math.factorial(N) * (1 - rho)))))
    prob_abandon = prob_wait * (1 - SLA) / SLA
    expected_wait_time = prob_wait * (staff[0] * (1 - rho)) / (A[0] * rho**N * math.factorial(N) / (N * (N - rho)**2))
    expected_service_time = (m / A[0] + AHT) / (1 - prob_wait)
    expected_time_in_system = expected_wait_time + expected_service_time
    return N, prob_wait, prob_abandon, expected_wait_time, expected_service_time, expected_time_in_system

#rho = A / (m * T)


# Input parameters
A = [100, 120, 150, 170, 100, 130, 160, 100, 150, 100, 150, 100, 150, 100, 150, 100]  # offered load
m = 50  # average number of agents per interval
SLA = 0.90  # service level agreement
AHT = 600  # average handle time (in seconds)
staff = [30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 55, 55, 60, 60, 65, 65]  # number of agents available per interval

# Calculate model outputs
N, prob_wait, prob_abandon, expected_wait_time, expected_service_time, expected_time_in_system = erlangC(A, m, SLA, AHT, staff)

# Print results
print("Results:")
print(f"Number of agents required: {N}")
print(f"Probability of waiting: {prob_wait:.4f}")
print(f"Probability of abandoning: {prob_abandon:.4f}")
print(f"Expected waiting time: {expected_wait_time:.2f} seconds")
print(f"Expected service time: {expected_service_time:.2f} seconds")
print(f"Expected time in system: {expected_time_in_system:.2f} seconds")