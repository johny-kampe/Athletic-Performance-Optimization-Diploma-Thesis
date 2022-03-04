from matplotlib import pyplot
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
# array_vec_1 = np.array([[12,41,60,11,21]])
# array_vec_2 = np.array([[40,11,4,11,14]])
# print(cosine_similarity(array_vec_1, array_vec_2))

names = ['Right shoulder x', 'Right shoulder y', 'Right elbow x', 'Right elbow y', 'Right wrist x', 'Right wrist y', 'Random']
# # Load dataset
dataset = pd.read_excel('second_Test.xls', names=names)

X = dataset.drop(columns=['Random'])  # getting right shoulder's coordinates (x, y)
y = dataset['Random']  # getting right elbow's coordinates (x, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# model = LinearRegression()  # %
# model = DecisionTreeClassifier()  # 66% 0.2, 64% 0.3, 63% 0.4
model = KNeighborsClassifier()  # 67% 0.2, 69% 0.3, 67% 0.4
# model = LinearDiscriminantAnalysis()  # 44% 0.2, 45% 0.3, 45% 0.4
# model = GaussianNB()  # 59% 0.2, 59% 0.3, 61% 0.4
# model = SVC(gamma='auto')  # 48% 0.2, 45% 0.3, 44% 0.4
# model = LogisticRegression()  # 42% 0.2, 45% 0.3, 0.41% 0.4
# model = MultinomialNB()  # 41% 0.2, 42% 0.3, 44% 0.4


model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)

print(score)



