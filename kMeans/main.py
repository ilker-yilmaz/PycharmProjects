import inline as inline
import matplotlib as matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

data = 'C:/Users/eymen/Desktop/Live.csv'

df = pd.read_csv(data)

print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())

df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)
print(df.info())

print(df.describe())

# view the labels in the variable
print(df['status_id'].unique())

# view how many different types of variables are there

print(len(df['status_id'].unique()))


# view the labels in the variable
print(df['status_published'].unique())

# view how many different types of variables are there

print(len(df['status_published'].unique()))

# view the labels in the variable

print(df['status_type'].unique())


# view how many different types of variables are there

print(len(df['status_type'].unique()))

df.drop(['status_id', 'status_published'], axis=1, inplace=True)

print(df.info())


print(df.head())


# declare feature vector and target variable
X = df

y = df['status_type']

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

X['status_type'] = le.fit_transform(X['status_type'])

y = le.transform(y)

print(X.info())

print(X.head())

#Feature Scaling
cols = X.columns
from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
X = ms.fit_transform(X)

X = pd.DataFrame(X, columns=[cols])

print(X.head())

#K-Means model with two clusters
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0)

kmeans.fit(X)

#K-Means model parameters study

kmeans.cluster_centers_

print(kmeans.inertia_)


#Check quality of weak classification by the model
labels = kmeans.labels_

# check how many of the samples were correctly labeled
correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))

print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))

#Use elbow method to find optimal number of clusters
from sklearn.cluster import KMeans
cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()




from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2,random_state=0)

kmeans.fit(X)

labels = kmeans.labels_

# check how many of the samples were correctly labeled

correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))

print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))


#K-Means model with different clusters
#K-Means model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

kmeans.fit(X)

# check how many of the samples were correctly labeled
labels = kmeans.labels_

correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))



#K-Means model with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=0)

kmeans.fit(X)

# check how many of the samples were correctly labeled
labels = kmeans.labels_

correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))