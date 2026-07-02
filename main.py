import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------------------------------
# Load Dataset
# ---------------------------------
df = pd.read_csv("preprocessed_data.csv")

print("="*60)
print("DATA PREVIEW")
print("="*60)
print(df.head())

# ---------------------------------
# ================================
# 1. SIMPLE LINEAR REGRESSION
# ================================
# ---------------------------------

print("\n" + "="*60)
print("SIMPLE LINEAR REGRESSION (RM vs MEDV)")
print("="*60)

# Feature and target
X_simple = df[['RM']]
y = df['MEDV']

# Split
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_simple, y, test_size=0.2, random_state=42
)

# Train model
simple_model = LinearRegression()
simple_model.fit(X_train_s, y_train_s)

# Predict
y_pred_s = simple_model.predict(X_test_s)

# Evaluation
print("MAE :", mean_absolute_error(y_test_s, y_pred_s))
print("MSE :", mean_squared_error(y_test_s, y_pred_s))
print("R2  :", r2_score(y_test_s, y_pred_s))

# Plot regression line
plt.figure(figsize=(7,5))
plt.scatter(X_test_s, y_test_s, color='blue', label="Actual")
plt.plot(X_test_s, y_pred_s, color='red', label="Prediction Line")
plt.xlabel("RM (Average Rooms)")
plt.ylabel("MEDV (House Price)")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()


# ---------------------------------
# ================================
# 2. MULTIPLE LINEAR REGRESSION
# ================================
# ---------------------------------

print("\n" + "="*60)
print("MULTIPLE LINEAR REGRESSION (All Features)")
print("="*60)

# Features and target
X_multi = df.drop(columns=['MEDV'])
y_multi = df['MEDV']

# Split
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

# Train model
multi_model = LinearRegression()
multi_model.fit(X_train_m, y_train_m)

# Predict
y_pred_m = multi_model.predict(X_test_m)

# Evaluation
print("MAE :", mean_absolute_error(y_test_m, y_pred_m))
print("MSE :", mean_squared_error(y_test_m, y_pred_m))
print("R2  :", r2_score(y_test_m, y_pred_m))

# ---------------------------------
# Coefficients
# ---------------------------------
coeff_df = pd.DataFrame({
    "Feature": X_multi.columns,
    "Coefficient": multi_model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\nMODEL COEFFICIENTS")
print("="*60)
print(coeff_df)


# ---------------------------------
# Actual vs Predicted Plot
# ---------------------------------
plt.figure(figsize=(7,5))
plt.scatter(y_test_m, y_pred_m, alpha=0.6)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Multiple Linear Regression: Actual vs Predicted")

# Perfect line
plt.plot([y_multi.min(), y_multi.max()],
         [y_multi.min(), y_multi.max()],
         'r--')

plt.show()


# ---------------------------------
# Residual Plot
# ---------------------------------
residuals = y_test_m - y_pred_m

plt.figure(figsize=(7,5))
plt.hist(residuals, bins=30, edgecolor='black')
plt.title("Residual Distribution")
plt.xlabel("Error")
plt.show()

print("\nEDA + LINEAR REGRESSION COMPLETED SUCCESSFULLY!")