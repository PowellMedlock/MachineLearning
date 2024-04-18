from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

df = pd.read_csv('/home/somedgnrte/Documents/Dataset/glass.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=1))
print('accuracy is', accuracy_score(y_pred, y_test,))

df2 = pd.read_csv('/home/somedgnrte/Documents/Dataset/glass.csv')
X2 = df2.iloc[:, :-1].values
y2 = df2.iloc[:, -1].values
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=0)
classifier2 = SVC()
classifier2.fit(X_train2, y_train2)
y_pred2 = classifier2.predict(X_test2)
print(classification_report(y_test2, y_pred2, zero_division=1))
print('accuracy is', accuracy_score(y_pred2, y_test2))

type = ["Naive Bayes", "SVM"]
accuracy = [accuracy_score(y_pred, y_test,), accuracy_score(y_pred2, y_test2)]
colors = ['tab:red', 'tab:blue']

plt.bar(type, accuracy, color=colors, label='Accuracy processing glass.csv')
plt.show()

plt.pie(accuracy, labels=type, colors=colors,shadow=True, wedgeprops={'edgecolor': 'black'})
plt.show()





