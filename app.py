from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import json

app = Flask(__name__)

def add_sentence(sentID, the_sentence):
	sentence = {'sentence_id': sentID,
			'sentence': the_sentence
			}
	status = "success"
	try:
		redis_client.set(sentID, json.dumps(sentence))
	except RedisError:
		status = "fail"
	
	return status
	
	
def view_sentence(sentID):
	sentence = ''
	status = ""
	try:
		sentence = redis_client.get(sentID)
	except RedisError:
		status = "fail"
		
	if status is not 'fail' and sentence is not '':
		sentence = json.loads(sentence)
		status = "sentence ID: {}, the sentence: {}".format(
								sentence['sentence_id'],
								sentence['sentence'],
								)
	return status
	
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		details = request.form
		if details['form_type'] == 'add_sentence':
			return add_sentence(details['sentID'], details['the_sentence'])
			
		elif details['form_type'] == 'view_sentence':
			return view_sentence(details['sentID'])
	return render_template('index.html')

if __name__ == '__main__':
	redis_client = StrictRedis(host='redis', port=6379)
	app.run(host='0.0.0.0')
	
	
	
	
	