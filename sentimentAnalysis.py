import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


df = pd.read_csv('Reviews.csv')
df1 = df.drop(['Id', 'ProductId', 'UserId', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Time'], axis=1)
df1.head()

X = df1['Text']
y = df1['Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


text_clf = Pipeline([
     ('vect', CountVectorizer()),
     ('tfidf', TfidfTransformer()),
     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                           alpha=1e-3, random_state=42,
                           max_iter=5, tol=None))
 ])

text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
#accuracy_score(y_test, predicted)

string = input("Enter your sentence: ")
sentence = pd.Series(string)
predicted = text_clf.predict(sentence)
predicted