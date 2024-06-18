import random

def erlang_c(num_servers, traffic_intensity):
    # Erlang C formula for call centers
    numerator = (traffic_intensity ** num_servers) / factorial(num_servers)
    denominator = sum([(traffic_intensity ** i) / factorial(i) for i in range(num_servers + 1)])
    return numerator / denominator

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def monte_carlo_simulation(num_servers, traffic_intensity, num_simulations):
    total_waiting_time = 0
    for _ in range(num_simulations):
        service_level = random.random()  # Random service level between 0 and 1
        # Find the minimum number of servers required to meet the service level
        for i in range(num_servers):
            if erlang_c(i, traffic_intensity) > service_level:
                break
        total_waiting_time += i / traffic_intensity
    average_waiting_time = total_waiting_time / num_simulations
    return average_waiting_time

if __name__ == "__main__":
    num_servers = 5
    traffic_intensity = 100
    num_simulations = 10000

    avg_waiting_time = monte_carlo_simulation(num_servers, traffic_intensity, num_simulations)
    print(f"Average waiting time: {avg_waiting_time:.2f} units of time")
