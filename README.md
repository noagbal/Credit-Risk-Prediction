# Credit-Risk-Prediction
This project aims to predict credit risk using various machine learning models. The dataset used for this project includes various features such as personal income, employment length, loan amount, and loan grade.

## Project Description
This project focuses on predicting the likelihood of a loan applicant defaulting on their loan. The prediction is made using various machine learning models, including:

- Logistic Regression
- Gaussian Naive Bayes
- K-Nearest Neighbors (KNN)
- Multi-Layer Perceptron (MLP)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Machines
- XGBoost
- LightGBM

## Dataset
The dataset used in this project is a publicly available credit risk dataset with the following features:

- person_age: Age of the applicant
- person_income: Annual income of the applicant
- person_emp_length: Employment length in years
- loan_amnt: Loan amount
- loan_int_rate: Loan interest rate
- loan_grade: Grade assigned to the loan
- loan_status: Whether the applicant defaulted (0) or not (1)

## Data Preprocessing
Before training the models, the dataset was preprocessed as follows:

- Addressed missing values in person_emp_length and loan_int_rate by imputing or dropping.
- Removed outliers in numerical features based on the interquartile range (IQR).
- Encoded categorical variables using LabelEncoder.
- Created additional features such as the ratio of age to income and the ratio of loan amount to income.

## Exploratory Data Analysis
Several plots and statistical analyses were conducted to understand the distribution of features and relationships between them:

- Bar plots for categorical variables.
- Scatter plots for relationships between income and loan amount.
- Box plots for comparing income across different loan grades.
- Heatmap for visualizing correlations among numerical features.

## Modeling
Multiple machine learning models were trained and evaluated:

- Logistic Regression
- Gaussian Naive Bayes
- K-Nearest Neighbors (KNN)
- Multi-Layer Perceptron (MLP)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Machines
- XGBoost
- LightGBM

Each model was fine-tuned using techniques such as Grid Search with Cross-Validation.

## Model Evaluation
The performance of each model was evaluated using metrics such as accuracy, F1 score, confusion matrix, and classification report. The best model was selected based on these evaluation metrics.

## Usage
To run the project, execute the following command:
streamlit run multi_page.py
