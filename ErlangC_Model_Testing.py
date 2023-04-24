import math

def erlangC(A, N, m, T, t0):
    """
    Calculates the Erlang C formula given the arrival rate, number of agents, service rate, time period, and start time.

    Parameters:
    A (list of floats): Arrival rate for each time interval (calls per hour)
    N (int): Number of agents
    m (float): Service rate (calls per hour per agent)
    T (float): Time period (in hours)
    t0 (float): Start time (in hours from midnight)

    Returns:
    list of floats: The probability that a call will have to wait in queue for each time interval.
    """
    result = []
    for i in range(len(A)):
        t1 = t0 + T # End time of interval i
        p = A[i] / (N * m) # Traffic intensity for interval i
        numerator = (N * p) ** N
        denominator = math.factorial(N) * (1 - p)
        for j in range(0, N):
            numerator += ((N * p) ** j) / math.factorial(j)
        prob = numerator / denominator
        result.append(prob)
        t0 = t1 # Update start time for next interval
    return result

# Example usage
A = [25, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 120, 130, 140, 140, 130, 120, 100, 90, 80, 70, 60, 50, 40] # Arrival rates for each half-hour interval
N = 10 # 10 agents
m = 20 # Service rate of 20 calls per hour per agent
T = 0.5 # Time period is half hour
t0 = 8.0 # Start time is 8am
result = erlangC(A, N, m, T, t0)
for i in range(len(result)):
    print(f"Probability of waiting in queue for interval {i+1}: {result[i]}")