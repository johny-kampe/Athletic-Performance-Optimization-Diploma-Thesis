import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import spatial
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
from math import sqrt


def calculate_similarity(dataset_correct, dataset_A):

    # array_vec_1 = np.array([[12, 41, 60, 11, 21]])
    # array_vec_2 = np.array([[40, 11, 4, 11, 14]])
    # print(cosine_similarity(array_vec_1, array_vec_2))

    count = 0

    #  DATASET CORRECT
    shoulderx_corr = dataset_correct["Right shoulder x"]
    shouldery_corr = dataset_correct["Right shoulder y"]

    elbowx_corr = dataset_correct["Right elbow x"]
    elbowy_corr = dataset_correct["Right elbow y"]

    wristx_corr = dataset_correct["Right wrist x"]
    wristy_corr = dataset_correct["Right wrist y"]

    #  DATASET A
    shoulderxA = datasetA["Right shoulder x"]
    shoulderyA = datasetA["Right shoulder y"]

    elbowxA = datasetA["Right elbow x"]
    elbowyA = datasetA["Right elbow y"]

    wristxA = datasetA["Right wrist x"]
    wristyA = datasetA["Right wrist y"]

    #  COORDINATES
    shoulderx_list = np.arange(30).reshape(-1, 1)
    shouldery_list = []

    elbowx_list = []
    elbowy_list = []

    wristx_list = []
    wristy_list = []

    #  RESULTS
    shoulderx_list_res = []
    shouldery_list_res = []

    elbowx_list_res = []
    elbowy_list_res = []

    wristx_list_res = []
    wristy_list_res = []

    Alist = []

    # for i in shoulderx_corr:
    #     if count < 30:
    #         shoulderx_list[count] = i
    #     else:
    #         count = 0
    #         # array_vec_1 = np.array([shoulderx_list]).reshape(-1, 1)
    #         array_vec_2 = np.array([shoulderxA]).reshape(-1, 1)
    #         shoulderx_list_res.append(cosine_similarity(shoulderx_list, array_vec_2))
    #         print(f"similarity: {cosine_similarity(shoulderx_list, array_vec_2)}")
    #     count += 1

    for i in range(30):
        print(shouldery_corr[i])
        Alist.append(shouldery_corr[i])


    for i in shouldery_corr:
        if count < 30:
            shouldery_list.append(i)
            count += 1
        else:
            count = 0
            print(shouldery_list)
            # array_vec_1 = np.array([shouldery_list])
            # array_vec_2 = np.array([shoulderyA])
            # shouldery_list_res.append(cosine_similarity(array_vec_1, array_vec_2) * 100)
            result = 1 - spatial.distance.cosine(shouldery_list, Alist)
            print(f"Result: {result}")
            # cos_sim(shoulderx_list, Alist)
            shouldery_list = []

    #
    #
    # for i in elbowx_corr:
    #     if count < 30:
    #         elbowx_list.append(i)
    #     else:
    #         count = 0
    #         print(elbowx_list)
    #         array_vec_1 = np.array([elbowx_list])
    #         array_vec_2 = np.array([elbowxA])
    #         elbowx_list_res(cosine_similarity(array_vec_1, array_vec_2) * 100)
    #     count += 1
    #
    # count = 0
    # for i in elbowy_corr:
    #     if count < 30:
    #         shoulderx_list.append(i)
    #     else:
    #         count = 0
    #         print(elbowy_list)
    #         array_vec_1 = np.array([elbowy_list])
    #         array_vec_2 = np.array([elbowyA])
    #         elbowy_list_res(cosine_similarity(array_vec_1, array_vec_2) * 100)
    #         count += 1
    #
    # for i in wristx_corr:
    #     if count < 30:
    #         wristx_list.append(i)
    #     else:
    #         count = 0
    #         print(wristx_list)
    #         array_vec_1 = np.array([wristx_list])
    #         array_vec_2 = np.array([wristxA])
    #         wristx_list_res(cosine_similarity(array_vec_1, array_vec_2) * 100)
    #     count += 1
    #
    # for i in wristy_corr:
    #     if count < 30:
    #         wristy_list.append(i)
    #     else:
    #         count = 0
    #         print(wristy_list)
    #         array_vec_1 = np.array([wristy_list])
    #         array_vec_2 = np.array([wristyA])
    #         wristy_list_res(cosine_similarity(array_vec_1, array_vec_2) * 100)
    #     count += 1

    # for i in range(0, 30):
    #     shoulderx_list[i] /= 49
    #     shouldery_list[i] /= 49
    #
    #     elbowx_list[i] /= 49
    #     elbowy_list[i] /= 49
    #
    #     wristx_list[i] /= 49
    #     wristy_list[i] /= 49


def elbow_function_silhouette_score(dataset):
    #  calculate the number of clusters with elbow function
    wss = []
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=1)
        kmeans.fit(dataset)
        wss.append(kmeans.inertia_)

    plt.plot(range(1, 10), wss)
    plt.title('The Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Sum of squared distances')
    plt.show()

    #  calculate silhouette score of the dataset
    for i in range(2, 10):
        kmeans = KMeans(n_clusters=i, max_iter=100)
        kmeans.fit(dataset)
        score = silhouette_score(dataset, kmeans.labels_)
        print("For cluster: {}, the silhouette score is: {}".format(i, score))

    silhouette_coefficients = []
    for i in range(2, 10):
        kmeans = KMeans(n_clusters=i, max_iter=100)
        kmeans.fit(dataset)
        score = silhouette_score(dataset, kmeans.labels_)
        silhouette_coefficients.append(score)

    plt.plot(range(2, 10), silhouette_coefficients)
    plt.xticks(range(2, 10))
    plt.xlabel("number of clusters")
    plt.ylabel("Silhouette coefficient")
    plt.show()

    print('\n')


def show_plots(dataset):
    plt.scatter(dataset["Right shoulder x"], dataset["Right shoulder y"])  # plot the datasetΑ
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    plt.scatter(dataset["Right elbow x"], dataset["Right elbow y"])  # plot the datasetΑ
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    plt.scatter(dataset["Right wrist x"], dataset["Right wrist y"])  # plot the datasetΑ
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def find_clusters(dataset):
    km = KMeans(n_clusters=3)
    y_predicted = km.fit_predict(datasetB)
    dataset['cluster'] = y_predicted

    df1 = dataset[dataset.cluster == 0]
    df2 = dataset[dataset.cluster == 1]
    df3 = dataset[dataset.cluster == 2]

    plt.scatter(df1["Right shoulder x"], df1["Right shoulder y"], color='green')
    plt.scatter(df2["Right shoulder x"], df2["Right shoulder y"], color='red')
    plt.scatter(df3["Right shoulder x"], df3["Right shoulder y"], color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def kmeans_clustering_visualization(datasetB):
    to_plot_shoulderB = pd.concat([datasetB[["Right shoulder x", "Right shoulder y"]]], join='outer', axis=1)
    to_plot_elbowB = pd.concat([datasetB[["Right elbow x", "Right elbow y"]]], join='outer', axis=1)
    to_plot_wristB = pd.concat([datasetB[["Right wrist x", "Right wrist y"]]], join='outer', axis=1)

    # to_plot_shoulderC = pd.concat([datasetB[["Right shoulder x", "Right shoulder y"]]], join='outer', axis=1)
    # to_plot_elbowC = pd.concat([datasetB[["Right elbow x", "Right elbow y"]]], join='outer', axis=1)
    # to_plot_wristC = pd.concat([datasetB[["Right wrist x", "Right wrist y"]]], join='outer', axis=1)

    show_plots(datasetB)

    elbow_function_silhouette_score(to_plot_shoulderB)
    elbow_function_silhouette_score(to_plot_elbowB)
    elbow_function_silhouette_score(to_plot_wristB)

    find_clusters(to_plot_shoulderB)
    # find_clusters(to_plot_elbowB)
    # find_clusters(to_plot_wristB)


datasetA = pd.read_excel('dataset.xls')
datasetB = pd.read_excel('real_world_set_A.xls')
datasetC = pd.read_excel('real_world_set_B.xls')

# calculate_similarity(datasetA, datasetB)

kmeans_clustering_visualization(datasetB)
