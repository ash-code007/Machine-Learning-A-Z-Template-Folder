#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the mall dataset with pandas
dataset = pd.read_csv('Mall_Customers.csv')
X =dataset.iloc[:, [3,4]].values
               
#Using the elbow method to find the optimal numberof clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
     kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
     kmeans.fit(X)
     wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Applying k-means to the mall dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans =kmeans.fit_predict(X)

#Visualizing the results
plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0, 1], s =100, c ='red', label ='careful')
plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1, 1], s =100, c ='blue', label ='standard')
plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2, 1], s =100, c ='green', label ='target')
plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3, 1], s =100, c ='cyan', label ='careless')
plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4, 1], s =100, c ='magenta', label ='sensible')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow', label = 'Centroids')
plt.title('Cluster of clients')
plt.xlabel('Annual Income($)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()