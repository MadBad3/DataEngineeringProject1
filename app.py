from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
    	details = request.form
    	if details['form_type'] == 'view_sentence':
    		int_features = request.form.values()
    		sentence = pd.Series(int_features)
    		predicted = model.predict(sentence)
    		prediction_text='The sentiment of this sentence is {}'.format(predicted[0])
    		return prediction_text

    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)