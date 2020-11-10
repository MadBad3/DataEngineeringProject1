import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass

	def tearDown(self):
		pass

	def test_a_index(self):
		response = requests.get('http://localhost:5000')
		self.assertEqual(response.status_code, 200)

	def test_b_sentiment_result(self):	
		params = {
			'sentence': 'I hate this show !',
			'form_type': "view_sentence"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'The sentiment of this sentence is negative')

	def test_c_sentiment_result(self):	
		params = {
			'sentence': 'I like the movie !',
			'form_type': "view_sentence"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'The sentiment of this sentence is positive')

	def test_d_sentiment_result(self):	
		params = {
			'sentence': 'He is fine but not today',
			'form_type': "view_sentence"
		}
		response = requests.post('http://localhost:5000', data=params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'The sentiment of this sentence is neutral')
if __name__ == '__main__':
	unittest.main()