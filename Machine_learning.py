import pandas as pd
import math
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score,train_test_split
import pickle
import random


df = pd.read_csv('/Users/martinjames/Documents/Self-Research/Academic work 2024/Python Analysis/Data/WIKI-PRICES.csv')

print(df.head(5))
column_names =df.columns.tolist()
print(df.columns.tolist())

df= df[['adj_open','adj_high','adj_low', 'adj_close','adj_volume']]

df ['HL_PCT'] = (df['adj_high']-df['adj_close'])/df['adj_close']*100
df ['PCT_change'] = (df['adj_close']-df['adj_open'])/df['adj_open'] * 100

df = df[['adj_close','HL_PCT','PCT_change','adj_volume']]

forecast_col = 'adj_close'
df.fillna(-99999, inplace= True)

forecast_out = int(math.ceil(0.01*len(df)))


df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail(5))


# Define x and y
X= np.array(df.drop('label', axis = 1))
y = np.array(df['label'])
X= preprocessing.scale(X)

#Split the data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# 1. First: Create model and perform cross-validation
cv_scores= cross_val_score(model,X_train,y_train, cv=5)

# Print cross-validation results
print("Cross-validation scores:", cv_scores)
print("Mean CV score:", cv_scores.mean())
print("Standard deviation of CV scores:", cv_scores.std())

# 2. Second: Fit the model on entire training set
model.fit(X_train, y_train)

# 3. Finally: Save the fitted model
model = LinearRegression()
with open('linearregression.pickle', 'wb') as f:
    pickle.dump(model,f)

# Later when needed, load the model
pickle_in=open('linearregression.pickle','rb')
model =pickle.load (pickle_in)


# Evaluate on the test set
test_accuracy = model.score(X_test, y_test)
print("Test set accuracy:", test_accuracy)


# Programming the best fit
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
xs=np.array([1,2,3,4,5,6], dtype=np.float64)
ys=np.array([5,4,6,5,6,7],dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m=(((mean(xs)*mean(ys)) -mean(xs*ys)) /
       ((mean(xs)*mean(xs))-mean(xs**2)))
    b=mean(ys)-m*mean(xs)
    return m,b

# Calculating r-squared/coefficient of determination
def squared_error (ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)
def coeffecient_of_determination (ys_orig,ys_line):
    y_mean_line=[mean(ys_orig) in ys_orig]
    squared_error_regr =squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1-(squared_error_regr/squared_error_y_mean)


m,b=best_fit_slope_and_intercept(xs,ys)

print(m,b)

regression_line =[(m*x)+b for x in xs]

predict_x = 8
predict_y = (m*predict_x)+b
r_squared =coeffecient_of_determination(ys,regression_line)
print(f" The value of r_squared is : {r_squared}")

plt.scatter(xs,ys)
plt.scatter(predict_x, predict_y, color ='g')
plt.plot(xs,regression_line)
plt.show()


