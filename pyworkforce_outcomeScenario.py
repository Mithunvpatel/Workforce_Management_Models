from pyworkforce.scheduling import MinAbsDifference, MinRequiredResources

# Rows are the days, each entry of a row, is number of positions required at an hour of the day (24). 
required_resources = [
    [9, 11, 17, 9, 7, 12, 5, 11, 8, 9, 18, 17, 8, 12, 16, 8, 7, 12, 11, 10, 13, 19, 16, 7],
    [13, 13, 12, 15, 18, 20, 13, 16, 17, 8, 13, 11, 6, 19, 11, 20, 19, 17, 10, 13, 14, 23, 16, 8]
]

# Each entry of a shift,an hour of the day (24), 1 if the shift covers that hour, 0 otherwise
shifts_coverage = {"Morning": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   "Afternoon": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                   "Night": [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                   "Mixed": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]}

# Method One
difference_scheduler = MinAbsDifference(num_days=2,
                                        periods=24,
                                        shifts_coverage=shifts_coverage,
                                        required_resources=required_resources,
                                        max_period_concurrency=27,
                                        max_shift_concurrency=25)

difference_solution = difference_scheduler.solve()

# Method Two

requirements_scheduler = MinRequiredResources(num_days=2,
                                              periods=24,
                                              shifts_coverage=shifts_coverage,
                                              required_resources=required_resources,
                                              max_period_concurrency=27,
                                              max_shift_concurrency=25)

requirements_solution = requirements_scheduler.solve()

print("difference_solution :", difference_solution)

print("requirements_solution :", requirements_solution)