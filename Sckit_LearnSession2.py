import sklearn
from sklearn.datasets import load_iris
# print(load_iris())

df = load_iris(return_X_y=True)
# print(df)
X,y = load_iris(return_X_y=True)

from sklearn.linear_model import LinearRegression
Model = LinearRegression()

# model fitting
Model.fit(X,y)

# print(Model.predict(X))

# K- Nearest Neighbors
from sklearn.neighbors import KNeighborsRegressor
mod = KNeighborsRegressor()
mod.fit(X,y)
# print(mod.predict(X))


# Visualization
import matplotlib.pyplot as plt
pred =mod.predict(X)
plt.scatter(pred,y)
# plt.show()


# Dataframes
import pandas as pd
from sklearn.datasets  import fetch_openml
df= fetch_openml('titanic', version= 1, as_frame=True)['data']
print(df.info())

# Checking for missing values across every column
# print(df.isnull().sum())

# Visualizing null values
import seaborn as sns
sns.set_style('darkgrid')

# Calculating the percentage of missing variable per feature
miss_value_per = pd.DataFrame((df.isnull().sum()/len(df))*100)
miss_value_per.plot(kind='bar', title="Missing values in percentage", ylabel ='percentage', figsize=(10,10))
# plt.show()

# Dropping a feature- body has most missing/null values -Deleting a feature is never preferred coz it leads to generalization error
# print(f"The size of the dataset: {df.shape}")

df.drop(['body'], axis=1, inplace=True)
# print(f"The size of the dataset: {df.shape}")

# Value imputation (mean, mode and median) to handle the null variables- ML performs exceptionally well
from sklearn.impute import SimpleImputer
# Age column
print(f"Number of Null values before imputing: {df.age.isnull().sum()}")
imp = SimpleImputer(strategy='mean')
df['age'] = imp.fit_transform(df[['age']])
print(f"Number of Null values in age after imputing: {df.age.isnull().sum()}")

# Handling missing values for the entire dataset using a function
def get_parameters(df):
    parameters ={}
    for col in df.columns[df.isnull().any()]:
        if df[col].dtype== 'float64' or df[col].dtype== "int64" or df[col].dtype== "int32":
            strategy ="mean"
        else:
            strategy ="most_frequent"

        missing_values = df[col][df[col].isnull()].values[0]
        parameters[col]={"missing_values" : missing_values, "strategy": strategy}
    return parameters

parameters = get_parameters(df)
for col, param in parameters.items():
    missing_values = param['missing_values']
    strategy = param['strategy']
    imp =SimpleImputer(missing_values=missing_values,strategy=strategy)
    df[col] = imp.fit_transform(df[[col]]).ravel()











