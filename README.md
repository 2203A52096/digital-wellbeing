# digital-wellbeing

## Mental Health and Digital Behavior 

The dataset is taken from kaggle from https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-digital-behavior-20202024/data

### Problem Statement

The goal of this project is to **predict a user's `digital_wellbeing_score`** based on various features like:

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

* The dataset (`mental_health_digital_behavior_data.csv`) is loaded using `pandas`.
* It contains **500 rows** of user behavior and mental health scores from 2020–2024.

#### 2. **Data Exploration**

* Use `.info()`, `.describe()` and `.head()` to understand data types, ranges, and structure.
* Checked for null values or data inconsistencies.

#### 3. **Data Visualization**

* **Box plots** and **scatter plots** were used to inspect distributions and detect outliers.
* `seaborn` and `matplotlib` were used for visualizations.

#### 4. **Correlation Analysis**

* Used `.corr()` to analyze correlation of features with `digital_wellbeing_score`.
* Found that **anxiety\_level** was strongly negatively correlated.

#### 5. **Feature Selection**

* Selected all features except the target (`digital_wellbeing_score`) for training.

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

Used `train_test_split` to divide data into 80% training and 20% testing sets.

#### 8. **Model Evaluation**

Evaluated all models using:

* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

#### 9. **Feature Importance**

Used `RandomForestRegressor.feature_importances_` to rank the importance of each input variable in prediction.

---

### 📊 Results Summary

* **Linear Regression** is overfitting (R² ≈ 1.00).
* **Random Forest and XGBoost** performed well, showing robust predictions.
* **SVR and KNN** showed relatively lower performance, possibly due to dataset size or scaling.

---

