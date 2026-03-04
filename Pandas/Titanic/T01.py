import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

pd.options.display.max_columns = 8
pd.options.display.max_rows = 100


df = pd.read_csv("Titanic-Dataset.csv")

#print(df[["Age", "Survived"]])

#modello machine learning gli interessano solo numeri, no stringhe

df = df.drop(["Name", "Cabin", "Ticket", "Fare","Embarked"], axis = 1)
df ["Age"] = df["Age"].fillna(df["Age"].median())
#df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop(["SibSp", "Parch"], axis = 1)

df = pd.get_dummies(df,columns = ["Sex"], drop_first = True )

X = df.drop("Survived", axis = 1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = LogisticRegression(max_iter = 1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_pred)

for feature, coef in zip(X.columns, model.coef_[0]):
    print(feature, coef)

print("Train_accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:", cm)

cr = classification_report(y_test, y_pred)
print("Classification Report:", cr)

jack = {
    "Age": 20,
    "Pclasse":3,
    "Embarked_Q":1,
    "Embarked_S":0,
    "Sex_male": 1
}
rose = {
    "Age": 17,
    "Pclasse": 1,
    "Embarked_Q": 0,
    "Embarked_S": 1,
    "Sex_male": 0

}

char_titanic_movie  = pd.DataFrame([jack,rose], index = ["Jack", "Rose"])
char_titanic_movie = char_titanic_movie.reindex(columns = X.columns, fill_value = 0)

pred_class = model.predict(char_titanic_movie)
pred_proba = model.predict_proba(char_titanic_movie)[:, 1]

results = pd.DataFrame({
    "Predicted Survived": pred_class,
    "Predicted Probability": pred_proba},index = char_titanic_movie.index)
print(results)
