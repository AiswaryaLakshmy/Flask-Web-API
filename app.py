from flask import Flask, jsonify, make_response, request
from flask_restful import Resource, Api, abort
import requests

app = Flask(__name__)
api = Api(app)

# abort if keyword is blank
def abort_if_keyword_blank(keyword):
	if keyword is None:
		abort(404, message="Please provide a keyword or enter in url using the format: /?keyword=valid_keyword")

# abort if no data found using the given keyword
def abort_if_final_result_none(final_result, keyword):
	if final_result is None:
		abort(404, message="Data not found using the given keyword: "+keyword)

@app.errorhandler(404) 
# inbuilt function which takes error as parameter
def not_found(e):
	return {'message': 'Please provide a keyword or enter in url using the format: /?keyword=valid_keyword'}, 404

class NYPLapi(Resource):
	def get(self):
		keyword = request.args.get('keyword')
		abort_if_keyword_blank(keyword)

		# NYPL Digital Collections API specified call from a background application using the token
		url = 'http://api.repo.nypl.org/api/v1/items/search?q='+ keyword +'&publicDomainOnly=true'
		auth = 'Token token=55kyp8iux7zjpbbh'
		call = requests.get(url, headers={'Authorization': auth})

		json_object = call.json()
		result1 = json_object.get('nyplAPI')
		result2 = result1.get('response')
		final_result = result2.get('result')

		abort_if_final_result_none(final_result, keyword)

		# to show the title and link to the NYPL books according to the keyword given without duplicate data
		temp, output = [], []
		for entry in final_result:
			title = entry["title"]
			if title not in temp:
				temp.append(title)
				output.append({"title": title, "itemLink": entry["itemLink"]})

		# return output in json format
		return make_response(jsonify(data=output), 200)

api.add_resource(NYPLapi, "/")

if __name__ == "__main__":
	app.run()
