# Лінійна регресія — це метод машинного навчання
# для прогнозування числових значень. Вона шукає
# лінійну залежність між вхідними даними (ознаками)
# та результатом, який ми хочемо передбачити.

from numpy.matlib import rand
import pandas as pd
import kagglehub
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


path = kagglehub.dataset_download("shivam2503/diamonds")
path_to_csv = os.path.join(path, "diamonds.csv")
df = pd.read_csv(path_to_csv)
# print(df)
X = df[['carat', 'depth', 'table', 'x', 'y', 'z']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R² Score:", r2)