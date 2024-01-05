
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Simulating data (replace this with your actual data)
data = {'Hour': [9, 10, 11, 12, 13, 14, 15, 16, 17],
        'Volume': [100, 150, 200, 250, 300, 325, 275, 225, 125]}

df = pd.DataFrame(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['Hour']], df['Volume'], test_size=0.2, random_state=42)

# Initialize and train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Visualize the results
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, predictions, color='blue', linewidth=3)
plt.xlabel('Number of Hours')
plt.ylabel('Volume')
plt.title('Predicting Volume based on Hours')
plt.show()