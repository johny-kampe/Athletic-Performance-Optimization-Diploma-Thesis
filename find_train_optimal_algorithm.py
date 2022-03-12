from pandas import read_csv
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# names = ['Right shoulder x', 'Right shoulder y', 'Right elbow x', 'Right elbow y', 'Right wrist x', 'Right wrist y']
# # # Load dataset
# dataset = pd.read_excel('second_Test.xls', names=names)
#
# X = dataset.drop(columns=['Random'])  # getting right shoulder's coordinates (x, y)
# X = dataset[:,2]
# print(X)
# y = dataset['Right elbow x']  # getting right elbow's coordinates (x, y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# model = LinearRegression()  # %
# model = DecisionTreeClassifier()  # 66% 0.2, 64% 0.3, 63% 0.4
# model = KNeighborsClassifier()  # 67% 0.2, 69% 0.3, 67% 0.4
# model = LinearDiscriminantAnalysis()  # 44% 0.2, 45% 0.3, 45% 0.4
# model = GaussianNB()  # 59% 0.2, 59% 0.3, 61% 0.4
# model = SVC(gamma='auto')  # 48% 0.2, 45% 0.3, 44% 0.4
# model = LogisticRegression()  # 42% 0.2, 45% 0.3, 0.41% 0.4
# model = MultinomialNB()  # 41% 0.2, 42% 0.3, 44% 0.4


# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# score = accuracy_score(y_test, predictions)
# print(score)

# array_vec_1 = np.array([dataset])
# array_vec_2 = np.array([y])


import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

a = np.array([10, 5, 15, 7, 5])
b = np.array([5, 10, 17, 5, 3])
cosine = cosine_similarity(a.reshape(1, -1), b.reshape(1, -1))
print(cosine)

from matplotlib import pyplot as plt

df = pd.read_excel("real_world_set_A.xls")
x1 = df['Right shoulder x']
y1 = df['Right shoulder y']

# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")

df = pd.read_excel("real_world_set_B.xls")
x2 = df['Right shoulder x']
y2 = df['Right shoulder y']
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')
plt.scatter(x1, y1, "stars", color= "green",
            marker= "*")
plt.legend()
plt.show()
