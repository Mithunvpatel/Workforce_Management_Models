import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import t

# Generate example data
np.random.seed(0)
n = 100
x = np.arange(n)
y = 2 * x + np.random.normal(0, 10, n)

# Fit a linear regression model
X = sm.add_constant(x)  # Add a constant term
model = sm.OLS(y, X)
results = model.fit()

# New observation for which we want to predict and calculate confidence interval
new_x = 110
new_X = np.array([[1, new_x]])  # Add a constant term to the new observation

# Predict the value
forecast_value = results.predict(new_X)

# Get the standard error of the forecast
mse = results.mse_resid  # Mean squared error
nobs = len(x)
mean_x = np.mean(x)
x_variance = np.sum((x - mean_x) ** 2)
x_new_variance = (new_x - mean_x) ** 2
se_forecast = np.sqrt(mse * (1 + 1/nobs + x_new_variance / x_variance))

# Calculate the degrees of freedom
df = nobs - len(results.params)

# Calculate the critical value (for a 95% confidence interval)
alpha = 0.05
t_critical = t.ppf(1 - alpha/2, df)

# Calculate the confidence interval
lower_bound = forecast_value - t_critical * se_forecast
upper_bound = forecast_value + t_critical * se_forecast

print("Forecasted Value:", forecast_value)
print("Confidence Interval (95%):", (lower_bound, upper_bound))
