from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = request.form.values()
    sentence = pd.Series(int_features)
    predicted = model.predict(sentence)

    return render_template('index.html', prediction_text='The sentiment is: {}'.format(predicted))

if __name__ == "__main__":
    app.run(host='0.0.0.0')