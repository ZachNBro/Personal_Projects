from ucimlrepo import fetch_ucirepo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# Fetch dataset
phishing_websites = fetch_ucirepo(id=327)

# Data (as pandas dataframes)
X = phishing_websites.data.features
y = phishing_websites.data.targets.squeeze()

# Data Exploration
print(X.dtypes)  # Display the data type of each feature

print("\nMissing values in each column:\n", X.isnull().sum())  # Check for missing values

# Convert the feature names to a list for the DataFrame
feature_names = X.columns.tolist()

# Create DataFrame for visualizations
X_df = pd.DataFrame(X, columns=feature_names)

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
corr_matrix = X_df.corr() # Compute the correlation matrix

# Select the top 4 features positively and negatively correlated with phishing
top_positive_features = corr_matrix['result'].nlargest(5).index
top_negative_features = corr_matrix['result'].nsmallest(4).index

# Combine selected features
selected_features = top_positive_features.union(top_negative_features)

# Extract the correlation matrix for the selected features only
selected_corr_matrix = corr_matrix.loc[selected_features, selected_features]

# Plot the correlation heatmap of selected features (corrected version)
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

# Preprocessing
# Separate the features and target variable
X = X_df.drop('result', axis=1)  # Drop the target variable from features
y = X_df['result']               # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=100)

# Initialize the Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=100)

# Model Fitting
# Create hyperparameter grid
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [3, 5, 7, 10],
    'min_samples_leaf': [1, 2, 5, 10]
}

# Initialize and perform search for best hyperparameters by accuracy
grid_search = GridSearchCV(estimator=dt,
                           param_grid=param_grid,
                           cv=StratifiedKFold(n_splits=5),
                           scoring='accuracy',
                           n_jobs=-1,
                           verbose=1)

# Fit GridSearchCV
grid_search.fit(X_train, y_train)

# Results
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", grid_search.best_score_)

# Predict on the test set using the best estimator from GridSearchCV
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Compute and print the accuracy of the best model using the test data
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy of Best Model:", accuracy)

# Evaluation
# Create an instance of the confusion matrix and pass the testing and prediction
# data of the target variable
cm = confusion_matrix(y_test, y_pred)
print("\n", cm)

# View the classifcation report
print("\n", classification_report(y_test,y_pred))

# Plot the confusion matrix
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Plot ROC & AUC Curves
logit_roc_auc = roc_auc_score(y_test, best_model.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, best_model.predict_proba(X_test)[:, 1])
plt.figure()
plt.plot(fpr, tpr, label='Decision Tree (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.savefig('Decision_Tree_ROC')
plt.show()

pip install ucimlrepo
