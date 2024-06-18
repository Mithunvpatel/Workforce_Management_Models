import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Generate synthetic historical data with seasonal patterns
np.random.seed(0)
base_fte = np.random.randint(3000, 4500, 12)

# Adjust for seasonal patterns (higher during flu and allergy seasons)
flu_season_adjustment = np.array([1.2, 1.3, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1])
allergy_season_adjustment = np.array([1.0, 1.0, 1.0, 1.1, 1.2, 1.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

historical_data = base_fte * flu_season_adjustment * allergy_season_adjustment

# Convert historical data to a pandas DataFrame
months = pd.date_range(start='2023-01-01', periods=12, freq='M')
data = pd.DataFrame(historical_data, index=months, columns=['FTE'])

# Fit the Holt-Winters model
model = ExponentialSmoothing(data['FTE'], trend='add', seasonal='add', seasonal_periods=12).fit()

# Forecast the next 6 months
forecast = model.forecast(6)
forecast_months = pd.date_range(start='2024-01-01', periods=6, freq='M')
forecast_df = pd.DataFrame(forecast, index=forecast_months, columns=['FTE'])

# Combine historical data with forecasted data
combined_df = pd.concat([data, forecast_df])

# Calculate average daily FTE requirement
# Assuming each month has 30 days for simplicity
combined_df['Daily FTE'] = combined_df['FTE'] / 30

# Print the forecasted data and average daily FTE requirement
print("Historical and Forecasted FTE (Monthly):")
print(combined_df)
print("\nAverage Daily FTE Requirement for the forecast period:")
print(combined_df['Daily FTE'][-6:].mean())

# Output: combined_df for full data and daily FTE for last 6 months
historical_and_forecasted_fte = combined_df
average_daily_fte_requirement = combined_df['Daily FTE'][-6:].mean()
