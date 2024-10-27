from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from numpy.linalg import norm

# Fetch dataset
phishing_websites = fetch_ucirepo(id=327)

# Data (as pandas dataframes)
X = phishing_websites.data.features
y = phishing_websites.data.targets.squeeze()

# Data Exploration
print(X.dtypes)  # Display the data type of each feature
print("\nMissing values in each column:\n", X.isnull().sum())  # Check for missing values

# Create DataFrame for visualizations
X_df = X.copy()

# Check feature values and discover any variance
print(X_df.describe())

# Add the target variable to the DataFrame
X_df['result'] = y
print(y.value_counts())  # Check the distribution of the target variable

# Visualizations
# Bar chart for the distribution of the target variable
plt.figure(figsize=(8, 6))
sns.countplot(x=y)
plt.title('Distribution of Target Variable (Phishing)')
plt.xlabel('Phishing/Not Phishing')
plt.ylabel('Count')
plt.show()

# Heatmap to find the features most related to phishing
corr_matrix = X_df.corr()  # Compute the correlation matrix

# Select the top 4 features positively and negatively correlated with phishing
top_positive_features = corr_matrix['result'].nlargest(5).index
top_negative_features = corr_matrix['result'].nsmallest(4).index

# Combine selected features
selected_features = top_positive_features.append(top_negative_features).unique()

# Extract the correlation matrix for the selected features only
selected_corr_matrix = corr_matrix.loc[selected_features, selected_features]

# Plot the correlation heatmap of selected features
plt.figure(figsize=(12, 10))
sns.heatmap(selected_corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Selected Features')
plt.show()

# Visualize selected features
def plot_countplot(data, feature):
    plt.figure(figsize=(8, 6))
    sns.countplot(x=data[feature], hue=data[feature], palette='coolwarm', legend=False)
    plt.title(f'Count of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()

# Plot countplots for selected features
for feature in selected_features:
    if feature != 'result':  # Avoid plotting the target variable
        plot_countplot(X_df, feature)

# Create a new DataFrame to count occurrences of most correlated features
combined_counts = X_df.groupby(['shortining_service', 'https_token']).size().reset_index(name='count')

# Plotting
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='https_token', y='count', hue='shortining_service', data=combined_counts,
            palette='coolwarm')

# Create custom legend
handles, labels = ax.get_legend_handles_labels()
# Add the custom legend with the correct colors
plt.legend(handles, labels, title='Shortening Service')

# Customize the plot
plt.title('Frequency of Shortening Service by HTTPS Token')
plt.xlabel('HTTPS Token')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()

# Preprocessing
# Separate the features and target variable
X = X_df.drop('result', axis=1).values  # Drop the target variable from features
y = X_df['result']  # Target variable

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scale the features to have a mean of 0 and variance of 1

# Initialize lists to hold WSS (for Elbow method) and silhouette scores
wss = []  # List to store WSS for Elbow method
silhouette_scores = []  # List to store silhouette scores

# Calculate WSS and silhouette scores for a range of cluster numbers
cluster_range = range(2, 11)  # Trying between 2 to 10 clusters
for n_clusters in cluster_range:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X_scaled)  # Fit the KMeans model and predict cluster labels
    wss.append(kmeans.inertia_)  # Store the WSS
    silhouette_scores.append(silhouette_score(X_scaled, labels))  # Store the silhouette score

# Plot the Elbow method curve
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, wss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Total Within Sum of Squares (WSS)')
plt.grid(True)
plt.show()

# Plot the Silhouette scores to visualize the best K
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, silhouette_scores, marker='o', linestyle='--', color='green')
plt.title('Silhouette Scores for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()

# Choose the optimal number of clusters based on the maximum silhouette score
optimal_n_clusters = cluster_range[silhouette_scores.index(max(silhouette_scores))]
print(f'Optimal number of clusters based on silhouette score: {optimal_n_clusters}')

# Apply k-means with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_n_clusters, random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)  # Fit the k-means model

# Calculate the average distance for the optimal clusters
centroid = kmeans.cluster_centers_
average_distances = []

# Calculate the average distance between each point and its cluster center
for cluster in range(optimal_n_clusters):
    cluster_points = X_scaled[y_kmeans == cluster]
    avg_distance = np.mean(norm(cluster_points - centroid[cluster], axis=1))
    average_distances.append(avg_distance)

# Print the average distance for the optimal clusters
print(f'Average Distance for optimal {optimal_n_clusters} clusters: {average_distances}')

# Perform PCA for visualization (retaining 95% variance)
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

# Visualize the results using PCA with KMeans cluster labels
plt.figure(figsize=(10, 6))

# Create scatter plot for each cluster separately to assign individual labels
for i in range(optimal_n_clusters):
    plt.scatter(X_pca[y_kmeans == i, 0], X_pca[y_kmeans == i, 1],
                s=50, alpha=0.6, edgecolors='k', label=f'Cluster {i+1}')

plt.title(f'PCA Visualization of Clustering (K = {optimal_n_clusters})')
plt.grid(True)

# Plot k-means cluster centers
centers = pca.transform(kmeans.cluster_centers_)  # Transform cluster centers to PCA space
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5, marker='X', label='Cluster Centers')

# Add legends: One for clusters and one for cluster centers
plt.legend()  # This will show both cluster labels and the cluster centers
plt.show()

pip install ucimlrepo
