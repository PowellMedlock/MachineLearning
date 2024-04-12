import mpl_toolkits.mplot3d.art3d
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from mpl_toolkits.mplot3d import Axes3D
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# a. Apply PCA on CC dataset.
df = pd.read_csv('/home/somedgnrte/Downloads/datasets/CC GENERAL.csv')
x = df.iloc[:, [1, 2, 3, 4]]
y = df.iloc[:, -1]

scaler = StandardScaler()

# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.


x_scaler = scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca, columns=['Principle Component 1', 'Principle Component 2'])
finaldf = pd.concat([df2, df[['PAYMENTS']]], axis=1)

print(finaldf)
# b. Apply k-means algorithm on the PCA result and report your observation if the silhouette score has
# improved or not?
score = metrics.silhouette_score(x, y)
print(score)

nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(x)

# predict the cluster for each data point

y_cluster_kmeans = km.predict(x)

score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)

# Perform Scaling+PCA+K-Means and report performance

plt.figure(figsize=(7, 7))
plt.scatter(finaldf['Principle Component 1'], finaldf['Principle Component 2'],
            c=finaldf['PAYMENTS'], cmap='prism', s=5)
plt.xlabel('pc1')
plt.ylabel('pc2')

plt.Text(0, 0.5, 'pc2')
plt.show()

# Use pd_speech_features.csv
dataf = pd.read_csv('/home/somedgnrte/Downloads/datasets/pd_speech_features.csv')
x2 = dataf.iloc[:, [1, 2, 3, 4]]
y2 = dataf.iloc[:, -1]

svm = SVC(kernel='linear')
svm.fit(x2, y2)
svm.predict(x2)

# Perform Scaling
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)

# apply PCA
pca = PCA(3)
x_pca = pca.fit_transform(x_scaler)
dataf2 = pd.DataFrame(data=x_pca, columns=['Principle Component 1', 'Principle Component 2', 'Principle Component 3'])
finaldataf = pd.concat([dataf2, dataf], axis=1)

# Use SVM to report performance

fig = plt.figure(figsize=(9, 9))
axes = ax1 = fig.add_subplot(111, projection='3d')
axes.set_title('SVM + PCA Representation of Speech Features', size=14)
axes.scatter(finaldataf['Principle Component 1'], finaldataf['Principle Component 2'],
             finaldataf['Principle Component 3'], c=finaldataf['Principle Component 2'], cmap='prism', s=10)

axes.set_xlabel('pc1')
axes.set_ylabel('pc2')
axes.set_zlabel('pc3')

plt.show()

# 3. Apply Linear Discriminant Analysis (LDA) on Iris.csv dataset to reduce dimensionality of data tok=2.

dataf2 = pd.read_csv('/home/somedgnrte/Downloads/datasets/Iris.csv')

new_x = dataf2.iloc[:0, -1].values
new_y = dataf2.iloc[:, -1].values

lda = LDA()
lda.fit(new_x, new_y)

x_lda = lda.transform(new_x)

df4 = pd.DataFrame(data=x_lda)
lastdf = pd.concat([df4, df], axis=1)

print(lastdf)

# 4. Briefly identify the difference between PCA and LDA

# PCA is unsupervised and attempts to capture the most variance in the data.
# LDA is supervised and attempts to get the most class seperability.
