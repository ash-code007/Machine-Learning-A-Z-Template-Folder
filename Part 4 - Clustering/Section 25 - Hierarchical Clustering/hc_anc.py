#Hierarchical Clustering

#%reset -f

#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the mall dataset with pandas
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values
                
#Using the dendogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

#Fitting hierarchical clustering to the mall dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc =hc.fit_predict(X)

#Visualizing the results
plt.scatter(X[y_hc == 0,0], X[y_hc == 0, 1], s =100, c ='red', label ='careful')
plt.scatter(X[y_hc == 1,0], X[y_hc == 1, 1], s =100, c ='blue', label ='standard')
plt.scatter(X[y_hc == 2,0], X[y_hc == 2, 1], s =100, c ='green', label ='target')
plt.scatter(X[y_hc == 3,0], X[y_hc == 3, 1], s =100, c ='cyan', label ='careless')
plt.scatter(X[y_hc == 4,0], X[y_hc == 4, 1], s =100, c ='magenta', label ='sensible')
plt.title('Cluster of clients')
plt.xlabel('Annual Income($)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

