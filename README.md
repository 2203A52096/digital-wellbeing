# digital-wellbeing

## Mental Health and Digital Behavior 

The dataset is taken from kaggle from https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-digital-behavior-20202024/data

### Problem Statement

The goal of this project is to **predict a user's _digital_wellbeing_score_** based on various features like:

* screen time
* social media usage
* notifications received
* sleep hours
* mood and focus levels
* anxiety level

This helps in understanding how digital behavior affects mental wellness and can guide digital wellbeing recommendations.

---

### Project Workflow

#### 1. **Data Reading**

* The dataset (_mental_health_digital_behavior_data.csv_) is loaded using _pandas_.
* It contains **500 rows** of user behavior and mental health scores from 2020–2024.

#### 2. **Data Exploration**

* Use _.info()_, _.describe()_ and _.head()_ to understand data types, ranges, and structure.
* Checked for null values or data inconsistencies.

#### 3. **Data Visualization**

* **Box plots** and **scatter plots** were used to inspect distributions and detect outliers.
* _seaborn_ and _matplotlib_ were used for visualizations.

#### 4. **Correlation Analysis**

* Used _.corr()_ to analyze correlation of features with _digital_wellbeing_score_.
* Found that **anxiety\_level** was strongly negatively correlated.

#### 5. **Feature Selection**

* Selected all features except the target (_digital_wellbeing_score_) for training.

#### 6. **Data Preprocessing**

* No missing values, so minimal cleaning required.
* All features were numerical, so no encoding was needed.

#### 7. **Model Training**

Trained multiple regression models:

* **Linear Regression**
* **Random Forest Regressor**
* **XGBoost Regressor**
* **Support Vector Regressor (SVR)**
* **K-Nearest Neighbors Regressor (KNN)**

Used _train_test_split_ to divide data into 80% training and 20% testing sets.

#### 8. **Model Evaluation**

Evaluated all models using:

* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

#### 9. **Feature Importance**

Used _RandomForestRegressor.feature_importances__ to rank the importance of each input variable in prediction.

---

### Results Summary

* **Linear Regression** is overfitting (R² ≈ 1.00).
* **Random Forest and XGBoost** performed well, showing robust predictions.
* **SVR and KNN** showed relatively lower performance, possibly due to dataset size or scaling.

---

