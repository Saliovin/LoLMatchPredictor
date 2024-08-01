import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

models = {}
accuracy, precision, recall = {}, {}, {}

models['Logistic Regression'] = LogisticRegression()
models['Support Vector Machines'] = LinearSVC()
models['Decision Trees'] = DecisionTreeClassifier()
models['Random Forest'] = RandomForestClassifier()
models['Naive Bayes'] = GaussianNB()
models['K-Nearest Neighbor'] = KNeighborsClassifier()

scaler_train = StandardScaler()
scaler_test = StandardScaler()
scaler_wr = StandardScaler()
df = pd.read_csv("inputs/dataset.csv")

X = df.iloc[:, df.columns != "team1Win"]
y = df["team1Win"]
print(len(df[df.team1Win == True]))
X["p1win_rate"] = scaler_wr.fit_transform(df[["p1win_rate"]])
X["p2win_rate"] = scaler_wr.fit_transform(df[["p2win_rate"]])
X["p3win_rate"] = scaler_wr.fit_transform(df[["p3win_rate"]])
X["p4win_rate"] = scaler_wr.fit_transform(df[["p4win_rate"]])
X["p5win_rate"] = scaler_wr.fit_transform(df[["p5win_rate"]])
X["p6win_rate"] = scaler_wr.fit_transform(df[["p6win_rate"]])
X["p7win_rate"] = scaler_wr.fit_transform(df[["p7win_rate"]])
X["p8win_rate"] = scaler_wr.fit_transform(df[["p8win_rate"]])
X["p9win_rate"] = scaler_wr.fit_transform(df[["p9win_rate"]])
X["p10win_rate"] = scaler_wr.fit_transform(df[["p10win_rate"]])
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.25, random_state=1)
X_train = scaler_train.fit_transform(X_train)
X_test = scaler_test.fit_transform(X_test)

for key in models.keys():
    models[key].fit(X_train, y_train)
    predictions = models[key].predict(X_test)  
    accuracy[key] = accuracy_score(predictions, y_test)
    precision[key] = precision_score(predictions, y_test)
    recall[key] = recall_score(predictions, y_test)
 
df_model = pd.DataFrame(index=models.keys(), columns=['Accuracy', 'Precision', 'Recall'])
df_model['Accuracy'] = accuracy.values()
df_model['Precision'] = precision.values()
df_model['Recall'] = recall.values()

print(df_model)

