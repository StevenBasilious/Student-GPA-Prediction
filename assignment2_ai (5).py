# -*- coding: utf-8 -*-
"""Assignment2 AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13YqV4kQr0hY2GzVZCKVT6LjovAogeHJn

#**Section 1 – Data Collection and Preprocessing**

##**About the dataset**

The Dataset that has been choosen:

Predicting Students Grades
https://www.kaggle.com/code/annastasy/predicting-students-grades/input

The dataset has information about 2392 students including 15 features about their demographic, academic and extracurricular stuff and the main idea of this dataset is to predict the student performance outcomes based on these features.
A quick description about the features studentID a special number for every student to identify him, age is the age of every student, gender is encoded as integers that gives for example (1 for male and 0 for females), ethnicity is also encoded as integer and it show different ethnic groups, parentalEducation Encoded as integers and shows the different levels of parent education, studTimeWeekly representing how many hours per week that the student studies, absences the total number of days that each student absence, tutoring is about whether the student get tutoring or no (1 for yes, 0 for no). ParentalSupport Encoded as integers and represent how much of parental support, extracurricular represent the student if they involve in extracurricular  activities, sports Encoded as integers shows whether the student involve in any sports activity or no, music involved in music related activities, volunteering Encoded as binary shows if the student volunteer or no, GPA represent Grade Point Average (which will be the target) and it represent the academic performance of the students, Encoded as integers, shows the performance classification.
And from this dataset it will be used to predict the Student GPA.

Furthermore all the dataset is numerical and which makes it perfect for models to use this data to train and no need to Encode categorical variables.

##**Import the library**
"""

# Data Manipulation and Visualization Libraries
import pandas as pd  # For handling dataframes
import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For advanced visualizations

# Data Preprocessing Libraries
from sklearn.preprocessing import StandardScaler  # For feature scaling

# Machine Learning Model Selection and Evaluation Libraries
from sklearn.model_selection import train_test_split, GridSearchCV  # For splitting data and hyperparameter tuning
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score  # For model evaluation

# Machine Learning Models
from sklearn.linear_model import LinearRegression # liner regression model
from sklearn.ensemble import RandomForestRegressor  # Random Forest model for regression
from sklearn.linear_model import Ridge, LinearRegression  # Ridge and Linear Regression models

# Neural Network Libraries
from tensorflow.keras.models import Sequential  # To build the neural network model
from tensorflow.keras.layers import Dense, Dropout  # For adding layers and dropout to the neural network
from tensorflow.keras.optimizers import Adam  # Optimizer for the neural network

# Function to calculate accuracy and plot confusion matrix
from sklearn.metrics import confusion_matrix # Import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

"""##**Load data**"""

studentDataPerf = pd.read_csv('/content/Student_performance_data _.csv')
studentDataPerf

studentDataPerf = studentDataPerf.drop(['Volunteering'], axis=1)
studentDataPerf

"""Here it has been attempted to load a dataset named Student_performance_data _.csv using pandas and the command pd.read_csv() reads the CSV file into a pandas DataFrame. After it loads it will be able to read and explore it.
And in here studentDataPerf = studentDataPerf.drop(['Volunteering'], axis=1)  
Here the Volunteering column is removed because there is no need for it.
Also all dataset are numerical do not have a categorical features so categorical encoding will no be perform as it is not needed.

##**Check the missing values**
"""

print ("dataSet Info: ")
print (studentDataPerf.info())

"""For this we see some information about the dataset like number of rows and columns, column names with their respective data types, non-null columns to identify missing values in each column and finally the memory usage of the DataFrame."""

#another way to check the missing values
studentDataPerf.isnull().sum()

"""This is a method in pandas for quick identify the count of missing values in each column of the dataset"""

studentDataPerf.value_counts()

"""this to make sure that all the dataset is numerical and there is no need for Categorical Encoding and this has been checked from  .value_counts()"""

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(studentDataPerf.describe())

"""studentDataPerf.describe() make a statistical summary of all numerical columns in dataFrame it have mean for num of non null values, mean to get the average, std for Measures the variability of values in the column, min the smallest value in each column, 25% the values that below 25%, 50% the middle value for the column when it sorted, 75% the value that below 75% of the data falls, max the largest value in each column.

##**Data Splitting**

###**Data split into x and y**
"""

y = studentDataPerf['GPA']
y

x = studentDataPerf.drop('GPA', axis=1)
x

"""here the data has been split into x and y as x will have the feature values (input data) and y will have target variable (GPA)

###**Split data into training and testing sets**
"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 50)

# Display the sizes of the training and testing datasets
print("\nTraining set size:", len(x_train))
print("Testing set size:", len(x_test))

"""to Define Features and Target in this part we split the data features (column) into x and y as the y will be the part we want to predict (GPA) and will split it again into 80% for training and 20% of the data will be used for testing (test_size=0.2)and by this we use x_train, y_train to train the model and make sure that the module learns pattern from the dataset, and the x-test, y_test to evaluate the module performance on unseen data.

##**Scale numerical features**
"""

# Identify numerical columns to scale
numerical_features = ['StudyTimeWeekly', 'Absences', 'GPA']

# Initialize the scaler
scaler = StandardScaler()

# Scale the features
scaled_features = scaler.fit_transform(studentDataPerf[numerical_features])

# Add scaled features back to the dataset
scaled_data = studentDataPerf.copy()
scaled_data[numerical_features] = scaled_features

# Display the scaled data
print(scaled_data.head())

scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)

"""The Scale numerical features implemented to prepare the dataset for models of machine learning that we will use and two of those models (Linear Regression and Neural Network) will get benefit from those feature scaling because it will depend on distance metrics but for random forest it does not require the scaling feature it has been used StandardScaler to standardize the numerical features (StudyTimeWeekly, Absences, and GPA).

#**Section 2 – Model Selection and Training**

##**Neural Network**

Neural Network it act like the structure of the human brain, neural networks have layers of neurons ( coordinated nodes) these layers have input layer, hidden layer could be one or more, and output layer and some of the benefits of neural networks that it is powerful that it can learn from raw data without depending on any of extensive feature and it is a perfect  model for large dataset

###**build and Train the model**
"""

scaler = StandardScaler()
x_nn_train_pred = scaler.fit_transform(x_train)
y_nn_test_pred = scaler.transform(x_test)

model = Sequential()
# Input layer and one hidden layer
model.add(Dense(64, activation='relu', input_dim = x_nn_train_pred.shape[1]))
model.add(Dropout(0.2))  #to prevent overfitting

# Another hidden layer
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

# Output layer for regression
model.add(Dense(1, activation='linear'))  # Linear activation for regression tasks
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae']) # Compile the model

"""###**train the model**"""

history = model.fit(x_nn_train_pred, y_train, validation_split=0.2, epochs=50, batch_size=32, verbose=1)

"""##**Random Forest**

Random forest is a algorithm that merge multiple decision tree to predict the output, and it make that by build a multiple decision trees during the training and outputting the average prediction from all the trees,
As a result of that, the average prediction from multiple trees makes it less risk of overfitting compared to a single tree, also if given more attention on which features are more important to predict the target value and it can handle large datasets.
"""

# Define a parameter grid for Random Forest
paramGridRf = {
    'n_estimators': [50, 100, 200],           # Number of trees in the forest
    'max_depth': [None, 10, 20],              # Maximum depth of the trees
    'min_samples_split': [2, 5, 10]           # Minimum samples required to split a node
}

# Initialize and fit GridSearchCV for Random Forest Regressor
grid_search_rf = GridSearchCV(RandomForestRegressor(random_state=42), paramGridRf, cv=3, scoring='r2')
grid_search_rf.fit(x_train, y_train)

# Output the best parameters and the cross-validation score
print("\nBest Parameters for Random Forest:", grid_search_rf.best_params_)
print("Best Cross-Validation R2 Score for Random Forest:", grid_search_rf.best_score_)

"""This code aims to perform hyperparameter tuning for random forest regressor by using gradSearchCV.
It start by import Import Random Forest Regressor then it define parameters grid n_estimators for number of decision trees it test 50, 100, 200, max_depth for the depth of the tree, min_samples_split for for the minimum number that need to split and it test 2, 5, 10.
After that it set up GridSearchCV and fit this GridSearchCV to training data by train more than random forest using combination of hyperparameters that stated in paramGridRf and the purpose of this to identify the best combination of hyperparameter for the random forest which will also make the model perform better.

###**build and Train the model**
"""

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train, y_train)

"""##**Linear Regression**

Linear Regression
Is the simplest and the most widely used algorithm for regression data, and it assumes a linear relationship between the independent variables and target variables. It has benefits like being fast to compute, and works perfectly with linearly separable data when there is a linear relationship between target and features.
"""

param_grid = {'alpha': [0.1, 1.0, 10.0, 100.0]}
ridge = Ridge()
grid_search = GridSearchCV(ridge, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(x_train, y_train)

print("Best hyperparameters:", grid_search.best_params_)

"""The aim of this code is to perform hyperparameter tuning for ridge regression by using gridsearchCV so at first it imports ridge regression to help prevent overfitting then it sets up gridsearchCV  to perform a complete search over the hyperparameter grid.
It have parameters like ridge for model to tune, cv = 5 state 5 fold cross validation to evaluate the model performance,  scoring= ‘neg_mean_squared_error’ for scoring metric to evaluate the model performance and pram_grid to have the values
grid_search.fit(x_train, y_train) to fit the gridSearchCV to data train ridge models for Alpha values.

###**build and Train the model**
"""

lr = LinearRegression()
lr.fit(x_train, y_train)

"""#**Section 3 – Prediction and Evaluation**

##**Neural Network**

###**Applying the model to make a prediction**
"""

predictions = model.predict(X_test)
print("Predicted GPA:", predictions[:10].flatten())
print("Actual GPA:", y_test[:10].values)

"""This code to apply the neural network model and it compare the predict values and real values it use the neural network to create a prediction  (predictions) using (x_test) test dataset and it print 10 predicted next to the actual values from the (y_test) target dataset and by this it will be easy to visually how it is close the model predictions match the actual data.

###**Evaluate the Model**
"""

y_pred = model.predict(y_nn_test_pred)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred) #to measure the average squared difference between the actual y and predicted y values thats shows how far the model prediction from the true value
r2 = r2_score(y_test, y_pred) # to measure the proportion of variance in the target variable

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")

"""the code to evaluates how good the regression Neural Network model predications, the MSE is important to measures the errors of the prediction, on the other side the R2 evaluates how effectively the Neural Network model captures variability in the target variable, those two shows a clear understanding of the model and its accuracy.

##**Linear Regression**

###**Applying the model to make a prediction**
"""

y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)

predictions = lr.predict(X_test)
print("Predicted GPA:", predictions[:10].flatten())
print("Actual GPA:", y_test[:10].values)

"""this code is to create a prediction using a liner regression use (x_train) to predict the training dataset and (x_test), and those prediction will help to see the model performance on both training and test data.
predictions = lr.predict(X_test) create a prediction using (x_test) dataset.
print("Predicted GPA:", predictions[:10].flatten())
print("Actual GPA:", y_test[:10].values) to compare easily between the predict values and real values.

###**Evaluate Model Performance**
"""

lr_train_mes = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score (y_train, y_lr_train_pred)

lr_test_mes = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score (y_test, y_lr_test_pred)

lr_result = pd.DataFrame([['Linear Regression', lr_train_mes, lr_train_r2, lr_test_mes, lr_test_r2]],
               columns = ['Model', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2'])

lr_result

"""The code to evaluates how good the regression of Linear Regression
model predications, the MSE is important to measures the errors of the prediction, on the other side the R2 evaluates how effectively the Linear Regression model captures variability in the target variable, those two shows a clear understanding of the model and its accuracy.

##**Random Forest**

###**Applying the model to make a prediction**
"""

y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)

predictions = rf.predict(X_test)
print("Predicted GPA:", predictions[:10].flatten())
print("Actual GPA:", y_test[:10].values)

"""this code is to create a prediction using a Random Forest use (x_train) to predict the training dataset and (x_test), and those prediction will help to see the model performance on both training and test data. predictions = rf.predict(X_test) create a prediction using (x_test) dataset. print("Predicted GPA:", predictions[:10].flatten()) print("Actual GPA:", y_test[:10].values) to compare easily between the predict values and real values.

###**Evaluate Model Performance**
"""

rf_train_mes = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score (y_train, y_rf_train_pred)

rf_test_mes = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score (y_test, y_rf_test_pred)

rf_result = pd.DataFrame([['Random Forest', rf_train_mes, rf_train_r2, rf_test_mes, rf_test_r2]],
               columns = ['Model', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2'])

rf_result

"""The code to evaluates how good the regression of Random Forest model predications, the MSE is important to measures the errors of the prediction, on the other side the R2 evaluates how effectively the Random Forest model captures variability in the target variable, those two shows a clear understanding of the model and its accuracy.

##**compare between models**

here we will see which model perform better between Linear Regression, Neural Network, and Random Forest and will Apply the categorization to actual and predicted values as
We categorize the gpa input into three categories: high if it is equal to 3.5 or more, medium if it is between 2.5 and 3.5, low if it is under 2.5.
y_test_classes = y_test.apply(categorize_gpa)
Apply this function to each value in my test and by this we can know how good each model performs.
"""

def categorize_gpa(gpa):
    if gpa >= 3.5:
        return 'High'
    elif gpa >= 2.5:
        return 'Medium'
    else:
        return 'Low'

y_test_classes = y_test.apply(categorize_gpa)  # Actual GPA categories

y_nn_pred_classes = pd.Series(y_pred.flatten()).apply(categorize_gpa)  # Neural network predictions

y_lr_test_classes = pd.Series(y_lr_test_pred).apply(categorize_gpa)  # Linear regression predictions

y_rf_test_classes = pd.Series(y_rf_test_pred).apply(categorize_gpa)  # Random forest predictions

# Function to calculate accuracy and plot confusion matrix
def evaluate_model(y_true, y_pred_classes, model_name):
    # Accuracy
    accuracy = accuracy_score(y_true, y_pred_classes)
    print(f"{model_name} Accuracy: {accuracy}")

evaluate_model(y_test_classes, y_nn_pred_classes, "Neural Network")

evaluate_model(y_test_classes, y_lr_test_classes, "Linear Regression")

evaluate_model(y_test_classes, y_rf_test_classes, "Random Forest")

"""We prepare each model to predict the GPA value but with a categorize_gpa function that will change these predictions and will put them into the categorical classes that we have made (law,med,high). Then we have evaluate_modelfunction to evaluate how good the prediction classes match the actual GPA values (y_test_classes). After that the accuracy will be a calculator to measure the correct part that has been predicted GPA categories out of all predictions and that will be useful because we can compare between models performance quickle."""

# Categorize Neural Network predictions
y_nn_pred_classes = pd.Series(y_pred.flatten()).apply(categorize_gpa)

# Calculate Accuracy for Neural Network
nn_accuracy = accuracy_score(y_test_classes, y_nn_pred_classes)

y_lr_test_classes = pd.Series(y_lr_test_pred).apply(categorize_gpa)

# Calculate Accuracy for Linear Regression
lr_accuracy = accuracy_score(y_test_classes, y_lr_test_classes)

# Categorize Random Forest predictions
y_rf_test_classes = pd.Series(y_rf_test_pred).apply(categorize_gpa)

# Calculate Accuracy for Random Forest
rf_accuracy = accuracy_score(y_test_classes, y_rf_test_classes)

model_accuracies = pd.DataFrame({
    "Model": ["Neural Network", "Linear Regression", "Random Forest"],
    "Accuracy (%)": [nn_accuracy * 100, lr_accuracy * 100, rf_accuracy * 100]
})

print(model_accuracies)

"""another way to represent the accuracies of the model for better look and easy to compare between them and as we can see
The Neural Network is a less better thatn other models because of the small difference between Random Forest and Linear Regression.

#**Section 4 – Visualization and Insights**

##**Confusion Matrix**
"""

# Function to calculate accuracy and plot confusion matrix
def evaluate_model(y_true, y_pred_classes, model_name):


    conf_matrix = confusion_matrix(y_true, y_pred_classes, labels=['Low', 'Medium', 'High'])
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Low', 'Medium', 'High'], yticklabels=['Low', 'Medium', 'High'])
    plt.title(f"Confusion Matrix for {model_name}")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.show()

evaluate_model(y_test_classes, y_nn_pred_classes, "Neural Network")

evaluate_model(y_test_classes, y_lr_test_classes, "Linear Regression")

evaluate_model(y_test_classes, y_rf_test_classes, "Random Forest")

"""Then we have the confusion matrix which is useful to sum up how well the predicted classes, every cell in the matrix shows the prediction count by comparing the predicted labels and actual values, it will have the correct predictions on top-left to bottom-right. In the Visualization part it has been provided a heatmap that intuitive and color has been coded that to interpret the confusion matrix, and it have on its y axis true labels and on the x axis the predicted labels and at the end it have the model evaluation by calling each model by evaluate_model function.

##**Data visualization of prediction results**
"""

plt.figure (figure = (5,5))
plt.scatter(x=y_train, y= y_lr_train_pred, alpha = 0.4)

z = np.polyfit(y_train, y_lr_train_pred, 1)
p = np.poly1d(z)

plt.plot(y_train, p(y_train), '#F8766D')
plt.ylabel('Predicted GPA')
plt.xlabel('Actual GPA')
plt.title('Linear Regression Model')
plt.show()

plt.figure (figure = (5,5))
plt.scatter(x=y_train, y= y_lr_train_pred, alpha = 0.4)

z = np.polyfit(y_train, y_rf_train_pred, 1)
p = np.poly1d(z)

plt.plot(y_train, p(y_train), '#F8766D')
plt.ylabel('Predicted GPA')
plt.xlabel('Actual GPA')
plt.title('Random forest Model')
plt.show()

plt.scatter(y_test, y_pred, alpha=0.4)#sssssssss

plt.plot(y_train, p(y_train), '#F8766D')
plt.xlabel('Actual GPA')
plt.ylabel('Predicted GPA')
plt.title('Neural Networks Model')
plt.show()

"""##**Feature importance**

###**Random Forest Feature Importance Visualization**
"""

# Extract feature importances from the trained Random Forest model
rf_feature_importances = rf.feature_importances_

# Create a DataFrame for Random Forest feature importances
rf_importance_df = pd.DataFrame({
    'Feature': x.columns,
    'Importance': rf_feature_importances
}).sort_values(by='Importance', ascending=False)

# Plot the feature importances for Random Forest
plt.figure(figsize=(12, 8))
sns.barplot(data=rf_importance_df, x='Importance', y='Feature', palette='viridis')
plt.title("Feature Importances: Random Forest")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.show()

"""This shows the feature importance visualization for the random forest and what features it uses the most for the model to predict the target value (GPA).

###**Linear Regression Feature Importance Visualization**
"""

# Extract coefficients from the Linear Regression model
lr_coefficients = lr.coef_

# Create a DataFrame for Linear Regression feature coefficients
lr_importance_df = pd.DataFrame({
    'Feature': x.columns,
    'Coefficient': lr_coefficients
}).sort_values(by='Coefficient', ascending=False)

# Plot the coefficients for Linear Regression
plt.figure(figsize=(12, 8))
sns.barplot(data=lr_importance_df, x='Coefficient', y='Feature', palette='viridis')
plt.title("Feature Coefficients: Linear Regression")
plt.xlabel("Coefficient Value")
plt.ylabel("Features")
plt.show()

"""This shows the feature importance visualization for the Linear Regression and what features it uses the most for the model to predict the target value (GPA)."""