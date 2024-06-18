import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Mock data generation
np.random.seed(42)
num_samples = 1000

age = np.random.randint(18, 80, num_samples)
handle_time = np.random.randint(10, 180, num_samples)
gender = np.random.choice(['Male', 'Female'], num_samples)
province = np.random.choice(['Ontario', 'Quebec', 'British Columbia', 'Alberta'], num_samples)
city = np.random.choice(['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton'], num_samples)

# Create DataFrame
mock_data = pd.DataFrame({
    'age': age,
    'handle_time': handle_time,
    'gender': gender,
    'province': province,
    'city': city
})

# Select features for clustering
features = mock_data[['age', 'handle_time']]

# Normalize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=45)  # You can choose the number of clusters
mock_data['cluster'] = kmeans.fit_predict(features_scaled)

# Create a Dash app
app = dash.Dash(__name__)

# Create scatter plot
fig = px.scatter(mock_data, x='age', y='handle_time', color='cluster', 
                 hover_data=['gender', 'province', 'city'])

# Layout of the Dash app
app.layout = html.Div([
    html.H1("KNN Segment Analysis of Life Lab Tests Handle Time"),
    dcc.Graph(figure=fig),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
