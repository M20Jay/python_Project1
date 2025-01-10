from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd


# # Sample data
# data = pd.DataFrame({
#     'size':[100,1500,1200,1700],
#     'bedrooms':[2,3,2,4],
#     'price':[200000,300000,250000,350000]
# })
#
# X = data[['size','bedrooms']]
# y=data['price']
#
# #create and fit model
# model = LinearRegression()
# model.fit(X,y)
#
# # Analysis
# print("coefficients:")
# print(f"Size: ${model.coef_[0]:.2f} per sq ft")
# print(f"Bedrooms: ${model.coef_[1]:.2f} per bedroom")
# print(f"Base price: ${model.intercept_:.2f}")
#
# # Predict new house price
# new_house = [[1300,3]] #1300 sq ft, 3 bedrooms
# predicted_price = model.predict(new_house)
# print(f"\nPredicted price: ${predicted_price[0]:.2f}")
#
# #r-squared
# r2 =model.score(X,y)
# print(f"R-squared: {r2:.4f}")

# importing libraries
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Sample data: [size, bedrooms]
X=np.array([[1000,2],[1500,3],[2000,4],[1200,2],[1700,3]])
y=np.array([200000,300000,400000,220000,350000]) #House prices

# Create and fit model
model = LinearRegression()
model.fit(X,y)

# Get coefficients
print("Size impact: ${:.2f} per sq ft".format(model.coef_[0]))
print("Bedroom impact:${:.2f} per bedroom".format(model.coef_[1]))
print("Base price: ${:.2f}".format(model.intercept_))

# Calculate R-squared
r2 = model.score(X,y)
print("R-squared:", r2)


# Make predictions
new_house = [[1300,2]] # 1300 sq ft, 2 bedrooms
predicted_price = model.predict(new_house)

print("\nPredicted price for new house: ${:.2f}".format(predicted_price[0]))

#print equation
features_names =['Size', 'Bedrooms']
print(f"\nPrice = ${model.intercept_:2f}", end ='')
for i, coef in enumerate(model.coef_):
    print(f"+${coef:2f}*{features_names[i]}", end ="")
