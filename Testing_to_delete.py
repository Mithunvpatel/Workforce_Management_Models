import numpy as np
import pandas as pd
import statsmodels.api as sm

# Generate some example data
np.random.seed(0)
n = 100
x = np.arange(n)
y = 2 * x + np.random.normal(0, 10, n)

# Fit a linear regression model
X = sm.add_constant(x)  # Add a constant term
model = sm.OLS(y, X)
results = model.fit()

# Make predictions
forecast_values = results.predict(X)

# Calculate confidence intervals for the forecast
forecast_ci = results.get_prediction(X).conf_int()

# Plot the data, the forecast, and the confidence intervals
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Actual Data', color='blue')
plt.plot(x, forecast_values, label='Forecast', color='red')
plt.fill_between(x, forecast_ci[:, 0], forecast_ci[:, 1], color='pink', alpha=0.3, label='95% Confidence Interval')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Forecast with 95% Confidence Interval')
plt.legend()
plt.grid(True)
plt.show()
