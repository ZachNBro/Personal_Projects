import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve

# Fetch the dataset
spambase = fetch_ucirepo(id=94)

X = spambase.data.features  # Independent variables (word, symbol, and pattern count)
y = spambase.data.targets    # Dependent variable (Spam / Not Spam)

# Convert y to a Series for plotting; sns.countplot expects a one-dimensional input
y = y.squeeze()

# Data Exploration
print(X.dtypes)  # Display the data type of each feature

print("\nMissing values in each column:\n", X.isnull().sum())  # Check for missing values

# Convert the feature names to a list for the DataFrame
feature_names = X.columns.tolist()

# Create DataFrame for visualizations
X_df = pd.DataFrame(X, columns=feature_names)

# Summary statistics for numberical values
print(X_df.describe())

# Bar chart for the distribution of the target variable
plt.figure(figsize=(8, 6))
sns.countplot(x=y)
plt.title('Distribution of Target Variable (Spam/Not Spam)')
plt.xlabel('Spam / Not Spam')
plt.ylabel('Count')
plt.show()

# Heatmap to find the features most related to spam
# Add the target variable to the DataFrame
X_df['Spam'] = y

# Compute the correlation matrix
corr_matrix = X_df.corr()

# Select the top 8 features based on their correlation with the target variable
top_features = corr_matrix['Spam'].abs().sort_values(ascending=False).index[:9]

# Subset the correlation matrix for the top features
top_corr_matrix = corr_matrix.loc[top_features, top_features]

# Generate and show the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(top_corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True,
            square=True, linewidths=.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Top Features with Spam', fontsize=16)
plt.show()

# Function for plotting histograms
def plot_histogram(data, feature):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[feature], kde=True, bins=30)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()

# Function for plotting boxplots
def plot_boxplot(data, target, feature):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=target, y=data[feature])
    plt.title(f'{feature} by Spam/Not Spam')
    plt.xlabel('Spam / Not Spam')
    plt.ylabel(feature)
    plt.show()

# Plots for exploratory analysis
# Selected top features for visualizations
selected_features = ['word_freq_your', 'word_freq_free', 'word_freq_000',
                     'word_freq_remove', 'char_freq_$']

# Loop to pass parameters to plot functions
for feature in selected_features:
    plot_histogram(X_df, feature)
    plot_boxplot(X_df, y, feature)

# Preprocess the data
# Train-Test Split using 70% as training data and 30% testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7,
                                                    test_size=0.3, shuffle=True)

# Balance the Dataset
# Summarize class distribution before resampling
print("\nClass distribution before resampling:", Counter(y_train))

# Create an instance of the over sampler and set the strategy to minority
oversample = RandomOverSampler(sampling_strategy='minority')

# Fit and apply the transform directly to the training data
X_train, y_train = oversample.fit_resample(X_train, y_train)

# Summarize class distribution after resampling
print("Class distribution after resampling:", Counter(y_train))

# Standardize the dataset
# Create an instance of the standard scaler
scaler = StandardScaler()

# Fit on training data and transform both training and test data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the parameter grid
param_grid = {
    'max_iter': [10000, 20000],
    'class_weight': ['balanced', None],
    'solver': ['saga', 'liblinear'],
    'C': [0.1, 0.2, 0.4, 1.0]
}

# Create an instance of the logistic regression model
lr = LogisticRegression()

# Create an instance of the GridSearchCV with the model, parameter grid and
# cross-validation for accuracy comparison
grid_search = GridSearchCV(estimator=lr, param_grid=param_grid,
                           cv=StratifiedKFold(n_splits=5), scoring='accuracy', n_jobs=-1)

# Fit the grid search to the training data
grid_search.fit(X_train, y_train)

# Print the best parameters and the best score
print("\nBest Parameters:", grid_search.best_params_)
print("\nBest Cross-validation Score:", grid_search.best_score_)

# Use the best estimator found by grid search to make predictions on the test set
best_lr = grid_search.best_estimator_
y_pred = best_lr.predict(X_test)

# Compute and print the accuracy of the best model using the test data
accuracy = best_lr.score(X_test, y_test)
print("\nTest Accuracy of Best Model:", accuracy)

# Coefficients
# Get the coefficients from the best logistic regression model
coefficients = best_lr.coef_[0]
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients}) # Pair each feature name with its corresponding coefficient
coef_df = coef_df.reindex(coef_df.Coefficient.abs().sort_values(ascending=False).index) # Sort the DataFrame by the absolute value of the coefficients
print(coef_df)

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
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Plot ROC & AUC Curves
logit_roc_auc = roc_auc_score(y_test, best_lr.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, best_lr.predict_proba(X_test)[:, 1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()
