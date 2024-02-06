# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'SpendingScore': [20, 60, 15, 80, 25, 50, 10, 75, 30, 65],
    'Income': [50000, 80000, 20000, 120000, 30000, 70000, 15000, 100000, 40000, 90000]
}

df = pd.DataFrame(data)

# Select features for clustering
X = df[['SpendingScore', 'Income']]

# Choose the number of clusters (you can use techniques like the elbow method to find optimal k)
k = 3

# Apply KMeans clustering
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Visualize the clusters
plt.scatter(df['SpendingScore'], df['Income'], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.xlabel('Spending Score')
plt.ylabel('Income')
plt.title('Customer Segmentation')
plt.show()
