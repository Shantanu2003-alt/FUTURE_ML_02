Customer Churn Prediction System
A comprehensive machine learning project that predicts which customers are likely to stop using a service. This system helps businesses identify at-risk customers and take proactive retention measures.

Overview:
Customer churn prediction is crucial for businesses as retaining existing customers is significantly more cost-effective than acquiring new ones. This project implements multiple machine learning algorithms to predict customer churn with high accuracy and provides actionable insights for business decision-makers.

Key Objectives:
Predict customer churn probability with high accuracy
Identify key factors driving customer churn
Provide business insights through comprehensive visualizations
Enable proactive customer retention strategies

Features:
Multiple ML Models: Implements Logistic Regression, Random Forest, and XGBoost
Advanced Data Processing: Handles imbalanced datasets using SMOTE
Feature Engineering: Creates meaningful features like senior citizen flag and credit-balance ratio
Comprehensive Evaluation: ROC-AUC, confusion matrices, and classification reports
Feature Importance Analysis: Identifies key churn drivers
Risk Segmentation: Ranks customers by churn probability
Automated Visualizations: Generates publication-ready charts and graphs

Dataset:
The project uses the Bank Customer Churn Dataset from Kaggle which includes:
10,000 customers with 14 features
Customer demographics: Age, Gender, Geography
Account information: Credit Score, Balance, Products Number
Service usage: Tenure, Activity status
Target variable: Exited (1 = Churned, 0 = Retained)

Key Features:
CreditScore: Customer's credit score
Geography: Customer's location (France, Germany, Spain)
Gender: Customer's gender
Age: Customer's age
Tenure: Number of years as customer
Balance: Account balance
NumOfProducts: Number of products used
HasCrCard: Has credit card (1/0)
IsActiveMember: Active membership status (1/0)
EstimatedSalary: Customer's estimated salary
Exited: Target variable (1 = Churned, 0 = Retained)

Installation:

Prerequisites:
Python 3.7+
pip package manager

Required Libraries:
bashpip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn
Clone Repository
bashgit clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

View results: Check the outputs folder for generated visualizations and reports

Code Structure:
The main script follows this workflow:

Data Loading & Exploration:
Data Cleaning & Preprocessing
Feature Engineering
Train-Test Split
Handle Class Imbalance (SMOTE)
Model Training (3 algorithms)
Model Evaluation
Visualization Generation
Business Insights

Results:

Model Performance Summary:
XGBoost: Accuracy = 82.95%, ROC-AUC = 85.14%
Random Forest: Accuracy = 82.80%, ROC-AUC = 85.99%
Logistic Regression: Accuracy = 70.15%, ROC-AUC = 76.83%

Top Churn Drivers (Feature Importance):
Age - Older customers more likely to churn
Number of Products - Customers with fewer products at risk
Geography - Location-based churn patterns
Balance - Account balance correlation with churn
Credit Score - Financial health indicator

Business Insights:
High-Risk Segment: Customers aged 50+ with single product
Geographic Patterns: Germany shows highest churn rates
Balance Impact: Customers with very high or very low balances are at risk
Activity Correlation: Inactive members have 2x higher churn probability

📁 Project Structure:
customer-churn-prediction/
│
├── README.md
├── churn_prediction.py          # Main script
├── Churn_Modelling.csv         # Dataset
├── requirements.txt            # Dependencies
│
├── outputs/                    # Generated files
│   ├── roc_curves.png
│   ├── confusion_matrix_*.png
│   ├── feature_importance.png
│   └── model_reports/
│
└── docs/                       # Documentation
    ├── methodology.md
    └── business_insights.md

Technologies Used:
Python 3.8+: Core programming language
Pandas: Data manipulation and analysis
NumPy: Numerical computing
Scikit-learn: Machine learning library
XGBoost: Gradient boosting framework
Matplotlib/Seaborn: Data visualization
SMOTE: Handling imbalanced datasets
Jupyter Notebook: Development environment

Advanced Features:

Data Preprocessing:
Automated handling of categorical variables
Feature scaling and normalization
Missing value imputation
Outlier detection and treatment

Model Optimization:
Hyperparameter tuning
Cross-validation
Class imbalance handling
Feature selection

Evaluation Metrics:
ROC-AUC curves
Precision-Recall curves
Confusion matrices
Classification reports
Business impact metrics

Business Applications:

Use Cases:
Proactive Customer Retention: Identify at-risk customers before they churn
Targeted Marketing: Personalized retention campaigns
Resource Allocation: Focus retention efforts on high-value customers
Product Development: Improve products based on churn drivers
Customer Segmentation: Risk-based customer categorization

ROI Benefits:
Reduced Churn Rate: 15-25% improvement in retention
Cost Savings: 5x cheaper than acquiring new customers
Revenue Protection: Prevent revenue loss from churning customers
Improved CLV: Increase customer lifetime value