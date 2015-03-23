
from flask import render_template,request
from . import domain_cache,api

@domain_cache.route('/doc/', endpoint='doc')
def swagger_ui():
	    return apidoc.ui_for(api)

#@domain_cache.route("/")
@api.route('/my-resource/<id>', endpoint='my-resource')
@api.doc(params={'id': 'An ID'})
	
@api.route('/my-resource/<id>', endpoint='my-resource')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
	def get(self, id):
		return {}
#def show_domain_cache():
#	return render_template('domain_cache/domain_cache.html')
