
from flask import render_template,request
from . import api,Resource


	
@api.route('/my-resource/<id>', endpoint='my-resource')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
	def get(self, id):
		return {}
	@api.doc(responses={403: 'Not Authorized'})
	def post(self, id):
		api.abort(403)


#@api.route('/ipfilter/', endpoint='ipfilter')
#@api.doc()
#class IpFilter(Resource):
#	def get(self):
#		"ip filter get"
#		return {"ipfilter":"ipfilter get"}

#def show_domain_cache():
#	return render_template('domain_cache/domain_cache.html')
