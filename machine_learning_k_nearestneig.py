import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn import datasets


data=datasets.load_wine(as_frame=True)
print(data)

X=data.data
y=data.target
names = data.target_names

print(names)

# creating data frame
df=pd.DataFrame(X,columns=data.feature_names)
df['wine class'] = data.target
df['wine class'] = df['wine class'].replace({0:'class 0',1:'class 1',2:'class 2'})

# Alternatively
# df['wine class'] = df['wine class'].replace([0,1,2],['class 0','class 1','class 2'])
print(df.groupby('wine class').size())
#visualizing the distribution of data
sns.pairplot(df,hue='wine class', palette="Set2")
# plt.show()

#visualize if we have any null value for imputation purpose
# print(df.isnull().sum())

# Segregating Data into Training and Test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

# creating the KN classifier/ instance of KNN Model
from sklearn.neighbors import KNeighborsClassifier
import math # setting the K value = 7.34 round it 7
print(math.sqrt(len(y_test)))

# Creating KNN classifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
pred= knn.predict(X_test)

# Visualizing the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,pred))

# Our accuracy is so less =0.6481 because of varying data; we use a standard scaler to improve that
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn1=KNeighborsClassifier(n_neighbors=7, metric="euclidean")
knn1.fit(X_train_scaled,y_train)
pred1=knn1.predict(X_test_scaled)
print(accuracy_score(y_test,pred1))
