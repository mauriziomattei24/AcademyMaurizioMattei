import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, homogeneity_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# caricare il dataset
def load_data():
    iris = load_iris()
    return iris.data, iris.target, iris.feature_names, iris.target_names

# applicare KMeans e restituire i cluster
def apply_kmeans(X, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    return kmeans.predict(X), kmeans

# ridurre il dataset a due componenti principali
def reduce_dimensions(X):
    pca = PCA(n_components=2)
    return pca.fit_transform(X)

# visualizzare i cluster
def plot_clusters(X_pca, y_kmeans):
    plt.figure()
    sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=y_kmeans, palette="viridis", s=100, alpha=0.7)
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.show()

# calcolare e stampare le metriche di valutazione
def evaluate_clustering(y_true, y_pred):
    rand_index = adjusted_rand_score(y_true, y_pred)
    homogeneity = homogeneity_score(y_true, y_pred)
    print(f"Adjusted Rand Index: {rand_index}")
    print(f"Homogeneity Score: {homogeneity}")

def plot_confusion_matrix(y_true, y_pred, target_names):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=target_names, yticklabels=target_names)
    plt.title("Predict vs Actual")
    plt.xlabel("Predicted Cluster")
    plt.ylabel("Actual Cluster")
    plt.show()


# main
def main():
    X, y, feature_names, target_names = load_data()
    
    y_kmeans, kmeans = apply_kmeans(X, n_clusters=3)
    
    X_pca = reduce_dimensions(X)
    
    plot_clusters(X_pca, y_kmeans)
    
    evaluate_clustering(y, y_kmeans)

    plot_confusion_matrix(y, y_kmeans, target_names)

main()

