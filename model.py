import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv('Reviews.csv')
df.head()

df['sentiment'] = df['Score'].apply(lambda rating : 'positive' if rating > 3 else ('negative' if rating < 3 else 'neutral'))

def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":",  "!",'"'))
    return final

df['Text'] = df['Text'].apply(remove_punctuation)
df = df.dropna(subset=['Summary'])
df['Summary'] = df['Summary'].apply(remove_punctuation)

dfNew = df[['Summary','sentiment']]
dfNew.head()

X_train, X_test, y_train, y_test = train_test_split(dfNew['Summary'], dfNew['sentiment'], test_size=0.33, random_state=42)

text_clf = Pipeline([
     ('vect', CountVectorizer(token_pattern=r'\b\w+\b')),
     ('lr', LogisticRegression())
])

text_clf.fit(X_train, y_train)

predicted = text_clf.predict(X_test)
accuracy_score(y_test, predicted)

pickle.dump(text_clf, open('model.pkl','wb'))