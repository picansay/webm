#-*-coding:utf-8-*-

from flask import render_template,request
from . import api,Resource
import werkzeug

import log

	
@api.route('/my-resource/<id>', endpoint='my-resource')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
	def get(self, id):
		return {}
	@api.doc(responses={403: 'Not Authorized'})
	def post(self, id):
		api.abort(403)


ns = api.namespace('test', description='核心操作 API')
file_parser = api.parser()
file_parser.add_argument('enable_syn', type=werkzeug.datastructures.FileStorage, location='json')
@ns.route('/fileupload', endpoint='fileupload')
class TestFileUpLoad(Resource):
	@api.doc(parser=file_parser)
	def put(self):
		args = file_parser.parse_args()
                log.debug(args)
                return {}
#@api.route('/ipfilter/', endpoint='ipfilter')
#@api.doc()
#class IpFilter(Resource):
#	def get(self):
#		"ip filter get"
#		return {"ipfilter":"ipfilter get"}

#def show_domain_cache():
#	return render_template('domain_cache/domain_cache.html')
