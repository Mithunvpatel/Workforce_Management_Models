import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
import math

# Define parameters
start_date = datetime(2024, 1, 1)
end_date = start_date + timedelta(days=89)  # 90 days from start_date

# Define seasonal factors
flu_season_factor = [1.1, 1.2, 1.3, 1.5, 1.8, 2.0, 2.2, 2.0, 1.8, 1.5, 1.3, 1.2]  # Example flu season factor by month
allergy_season_factor = [1.2, 1.3, 1.5, 2.0, 2.5, 3.0, 3.0, 2.5, 2.0, 1.5, 1.3, 1.2]  # Example allergy season factor by month

# Convert seasonal factors to float
flu_season_factor = [float(factor) for factor in flu_season_factor]
allergy_season_factor = [float(factor) for factor in allergy_season_factor]

# Initialize empty lists to store data
dates = []
patient_ids = []
test_names = []

# Generate dummy data for each day
current_date = start_date
fte_list = []
required_staff = []
while current_date <= end_date:
    # Generate number of patients for the day (assuming random variation)
    num_patients = np.random.randint(50, 100)
    
    # Adjust patient volume based on seasonal factors
    month = current_date.month
    flu_factor = flu_season_factor[month - 1] if 1 <= month <= 12 else 1.0
    allergy_factor = allergy_season_factor[month - 1] if 1 <= month <= 12 else 1.0

    num_patients = int(num_patients * flu_factor * allergy_factor)
    
    # Calculate total time spent by patients for the day
    total_time_minutes = num_patients * 13.5  # Assuming each patient spends 13.5 minutes on average
    
    # Assuming 8 hours of work per day
    total_working_hours = 8
    
    # Calculate FTE for the day
    fte = total_time_minutes / (total_working_hours * 60)  # Convert total time to hours
    fte_list.append(fte)
    
    # Round FTE to the nearest whole integer to determine required staff
    required_staff.append(math.ceil(fte))
    
    # Generate patient IDs and test names for each patient
    for _ in range(num_patients):
        patient_ids.append(random.randint(1000, 9999))  # Example patient IDs
        test_names.append(random.choice(['Blood Test', 'Urine Test', 'X-Ray', 'MRI', 'Allergy Test', 'Flu Test']))
        dates.append(current_date)
    
    # Move to the next day
    current_date += timedelta(days=1)

# Create DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Patient_ID': patient_ids,
    'Test_Name': test_names
})

# Plotting
plt.figure(figsize=(12, 6))

# Plot customer demand FTE as a line chart
plt.plot(pd.date_range(start_date, end_date, freq='D'), fte_list, marker='x', color='black', linestyle='--', label='Customer Demand (FTE)')

# Plot staff scheduled FTE as a bar chart
plt.bar(pd.date_range(start_date, end_date, freq='D'), required_staff, color='green', label='Staff Scheduled (FTE)')

plt.title('Customer Demand vs Staff Scheduled (FTE) for 90 Days')
plt.xlabel('Date')
plt.ylabel('FTE')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------------