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
print(get_parameters(df))

# filling missing values in a DataFrame
parameters = get_parameters(df)
for col, param in parameters.items():
    missing_values = param['missing_values']
    strategy = param['strategy']
    imp =SimpleImputer(missing_values=missing_values,strategy=strategy)
    df[col] = imp.fit_transform(df[[col]]).ravel()

print(df.isnull().sum())


# Feature Engineering- process of selecting, manipulating and transforming raw data that can be used supervised learning
df['family'] = df['sibsp']+df['parch']

# Then create travelled_alone based on family size
df['travelled_alone'] = (df['family'] == 0).astype(int)

# df.loc[df['family']> 0, 'travelled_alone'] = 0
# df.loc[df['family']==1, 'travelled_alone'] = 1
df['travelled_alone'].value_counts().plot(kind='bar', title="Passenger travelled alone?", ylabel ='percentage', figsize=(10,10))
# plt.show()

#Data Encoding- transforming categorical features on a numerical scale on a continuous scale
# hot encoder create binary categories -Categories have no natural order (like colors: red, blue, green)
from sklearn.preprocessing import OneHotEncoder
# encoder =OneHotEncoder(sparse_output= False)
# encoded_sex=encoder.fit_transform(df[['sex']])
# df['female'] = encoded_sex[:,0]
# df['male'] = encoded_sex[:,1]

# OR Method 2: Using pandas get_dummies (simpler approach)
# sex_dummies =pd.get_dummies(df['sex'])
# df['female'] = sex_dummies['female']
# df['male'] = sex_dummies['male']

# Print the result
# print(df[['sex', 'female', 'male']])

# Label Encoder
# It would be ideal to have male and female date in one column thus use label encoder
# Categories have a natural order (like sizes: small→0, medium→1, large→2)

from sklearn.preprocessing import LabelEncoder

# Create and fit the encoder
le = LabelEncoder()

# Transform the sex column
df['sex_encoded']= le.fit_transform(df['sex'])
print(df[['sex_encoded']])

# Hot encoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Create and fit the encoder
encoder = OneHotEncoder(sparse_output=False)
encoded_array = encoder.fit_transform(df[['sex']])

# # Convert to DataFrame with meaningful column names
# encoded_df = pd.DataFrame(
#     encoded_array,
#     columns=encoder.get_feature_names_out(['sex'])
# )

# If you want to add these columns back to your original dataframe
# df = pd.concat([df, encoded_df], axis=1)

# Data Scaling - useful for reducing the distance between data point (far and closer)
# 1. Using Standard Scalar
from sklearn.preprocessing import StandardScaler
num_cols =df.select_dtypes(include=['int64', 'float64','int32']).columns
# print(num_cols)
print('Numerical columns:', list(num_cols))

ss = StandardScaler()
df[num_cols] = ss.fit_transform(df[num_cols])
print(df[num_cols].describe())

# 2. Using MinimaxScaler
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()
df[num_cols] = mm.fit_transform(df[num_cols])
print(df[num_cols].describe())

