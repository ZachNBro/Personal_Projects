import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
from imblearn.over_sampling import RandomOverSampler

# Fetch the dataset
spambase = fetch_ucirepo(id=94)

# Independent variables (word, symbol, and pattern count)
X = spambase.data.features

# Dependent variable (Spam / Not Spam)
y = spambase.data.targets.squeeze()

# Check for missing values
print("\nMissing values in each column:\n", X.isnull().sum())

# Convert the feature names to a list for the DataFrame
feature_names = X.columns.tolist()

# Create DataFrame for visualizations
X_df = pd.DataFrame(X, columns=feature_names)

# Bar chart for the distribution of the target variable
plt.figure(figsize=(8, 6))
sns.countplot(x=y)
plt.title('Distribution of Target Variable (Spam/Not Spam)')
plt.xlabel('Spam / Not Spam')
plt.ylabel('Count')
plt.show()

# Add the target variable to the DataFrame for correlation
X_df['Spam'] = y

# Compute the correlation matrix
corr_matrix = X_df.corr()

# Select the top 4 features positively and negatively correlated with spam
top_positive_features = corr_matrix['Spam'].nlargest(5).index 
top_negative_features = corr_matrix['Spam'].nsmallest(4).index  

# Combine selected features
selected_features = top_positive_features.union(top_negative_features)
X_selected = X_df[selected_features]

# Plot the correlation heatmap of selected features
plt.figure(figsize=(12, 10))
sns.heatmap(X_selected.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Selected Features')
plt.show()

# Visualize selected features
def plot_histogram(data, feature):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[feature], kde=True, bins=30)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()

def plot_boxplot(data, target, feature):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=target, y=data[feature])
    plt.title(f'{feature} by Spam/Not Spam')
    plt.xlabel('Spam / Not Spam')
    plt.ylabel(feature)
    plt.show()

# Plot histograms and boxplots for selected features
for feature in selected_features:
    if feature != 'Spam':  # Avoid plotting the target variable
        plot_histogram(X_df, feature)
        plot_boxplot(X_df, y, feature)

# Split the data into training and testing sets with only selected features
X_train, X_test, y_train, y_test = train_test_split(X_selected.drop(columns=['Spam']), y, train_size=0.7,
                                                    test_size=0.3, shuffle=True)

# Handle class imbalance using RandomOverSampler
oversampler = RandomOverSampler()
X_train, y_train = oversampler.fit_resample(X_train, y_train)

# Hyperparameter tuning with GridSearchCV
param_grid = {'alpha': [0.01, 0.1, 0.5, 1.0, 1.5, 2.0]}  # Different alpha values for smoothing
nb_model = MultinomialNB()
grid_search = GridSearchCV(nb_model, param_grid, cv=StratifiedKFold(n_splits=5), 
                           scoring='f1', n_jobs=-1)

# Fit the GridSearchCV to the data
grid_search.fit(X_train, y_train)

# Print the best parameters and the best cross-validation score
print("\nBest alpha:", grid_search.best_params_)
print("\nBest cross-validation F1 score:", grid_search.best_score_)

# Use the best estimator found by grid search to make predictions on the test set
best_nb = grid_search.best_estimator_
y_pred = best_nb.predict(X_test)

# Classification report
print(classification_report(y_test, y_pred))

# Confusion matrix visualization in a heatmap
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Spam', 'Spam'], yticklabels=['Not Spam', 'Spam'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

# Plot ROC & AUC Curves
roc_auc = roc_auc_score(y_test, best_nb.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, best_nb.predict_proba(X_test)[:, 1])
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, label='Naive Bayes (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
