# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Generate mock data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor with 10 trees
rf_regressor = RandomForestRegressor(n_estimators=10, random_state=42)

# Train the model
rf_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_regressor.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the results
plt.scatter(X_test, y_test, color='black', label='Actual data')
plt.scatter(X_test, y_pred, color='red', label='Predictions')

# Sort the test data for better visualization
sorted_indices = np.argsort(X_test.flatten())

# Plot the piecewise constant regression line
plt.step(X_test[sorted_indices], y_pred[sorted_indices], where='mid', color='blue', linestyle='-', linewidth=2, label='Regression line')

plt.legend()
plt.title('Random Forest Regression with Piecewise Constant Line of Best Fit')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

