# Student GPA Prediction

## Project Overview
This repository contains a machine learning project focused on predicting students' Grade Point Average (GPA) using a dataset of 2392 students. The dataset includes 15 features such as age, gender, study time per week, absences, parental support, and extracurricular activities. The project implements and compares three machine learning models—Neural Network, Random Forest Regressor, and Linear Regression—to identify the most effective approach for predicting GPA.

## Objectives
- Preprocess and analyze student performance data.
- Train and evaluate multiple machine learning models.
- Compare model performance using metrics like Mean Squared Error (MSE), R2 Score, and accuracy for categorized GPA (Low, Medium, High).
- Visualize results and feature importance to gain insights into factors affecting student performance.

## Dataset
The dataset is sourced from [Kaggle](https://www.kaggle.com/code/annastasy/predicting-students-grades/input) and contains numerical features, eliminating the need for categorical encoding. Key features include:
- `studentID`: Unique identifier for each student.
- `age`: Student's age.
- `gender`: Encoded as 0 or 1 (e.g., 0 for female, 1 for male).
- `studyTimeWeekly`: Hours spent studying per week.
- `absences`: Number of days absent.
- `GPA`: Target variable representing academic performance.

## Project Structure
- **Data Preprocessing**:
  - Loads the dataset and removes irrelevant features (e.g., 'Volunteering').
  - Checks for missing values and scales numerical features using `StandardScaler`.
  - Splits data into 80% training and 20% testing sets.
- **Model Training**:
  - **Neural Network**: Built with TensorFlow/Keras, including two hidden layers with dropout to prevent overfitting.
  - **Random Forest Regressor**: Optimized using GridSearchCV for hyperparameters like `n_estimators` and `max_depth`.
  - **Linear Regression**: Uses Ridge regularization with tuned `alpha` values.
- **Evaluation**:
  - Models are evaluated using MSE, R2 Score, and accuracy based on GPA categories (Low: <2.5, Medium: 2.5–3.5, High: ≥3.5).
- **Visualization**:
  - Confusion matrices for model performance.
  - Scatter plots comparing predicted vs. actual GPA.
  - Feature importance visualizations for Random Forest and Linear Regression.

## Requirements
To run this project, install the following Python libraries:
```bash
pip install pandas numpy scikit-learn tensorflow matplotlib seaborn
