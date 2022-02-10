try:
	import unittest
	from app import app
	from flask import Flask, request

except Exception as e:
	print("Some Modules are Missing {} ".format(e))

class FlaskTest(unittest.TestCase):

	# test for index function in app 
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/?keyword=cats')
		self.assertEqual(response.content_type, "application/json")
		self.assertEqual(response.status_code, 200)

	with app.test_request_context('/?keyword=cats'):
		assert request.path == '/'
		assert request.args['keyword'] == 'cats'

	# test for index function with valid keyword
	def test_index_with_keyword(self):
		tester = app.test_client(self)
		response = tester.get('/?keyword=cats')
		data = response.get_data(as_text=True)
		self.assertIn('data', data)
		self.assertEqual(response.content_type, "application/json")
		self.assertEqual(response.status_code, 200)

	# test for index function without a valid keyword
	def test_index_without_keyword(self):
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertTrue(b'Please provide a keyword or enter in url using the format: /?keyword=valid_keyword' in response.data)
		self.assertEqual(response.status_code, 404)

	# test for invalid route format
	def test_invalid_route(self):
		tester = app.test_client(self)
		response = tester.get('/cats')
		self.assertTrue(b'Please provide a keyword or enter in url using the format: /?keyword=valid_keyword' in response.data)
		self.assertEqual(response.status_code, 404)

	# test for index function with invalid keyword
	def test_index_invalid_keyword(self):
		tester = app.test_client(self)
		response = tester.get('/?keyword=jgjjhghghj')
		self.assertTrue(b'Data not found using the given keyword: jgjjhghghj' in response.data)
		self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
	unittest.main()
