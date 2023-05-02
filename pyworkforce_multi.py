from pyworkforce.queuing import MultiErlangC

param_grid = {"transactions": [100], "aht": [3], "interval": [30], "asa": [20 / 60], "shrinkage": [0.3]}
multi_erlang = MultiErlangC(param_grid=param_grid, n_jobs=-1)

required_positions_scenarios = {"service_level": [0.8, 0.85, 0.9], "max_occupancy": [0.8]}

positions_requirements = multi_erlang.required_positions(required_positions_scenarios)
print("positions_requirements: ", positions_requirements)