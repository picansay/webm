#-*-coding:utf-8-*-

import log
from . import api,Resource
from core_version import get_core_version
from core_ip_rules import get_ip_rules,post_ip_rules,del_ip_rules


ns = api.namespace('core', description='核心操作 API')

parser = api.parser()
parser.add_argument('ip_rules', type=str, required=True, help='IP范围', location='form')
#parser.add_argument('ip_rules', type=str, action='append',required=True, help='IP范围', location='form')

@ns.route('/version/', endpoint='version')
class Version(Resource):
	def get(self):
		'''ip filter get'''
		return get_core_version()

@ns.route('/ip_rules/', endpoint='ip_rules')
class IpRules(Resource):
	def get(self):
		'''ip rules get'''
		return get_ip_rules()
	@api.doc(parser=parser)
	def post(self):
		'''ip filter post'''
		args = parser.parse_args()
                log.debug(args)
		return post_ip_rules(args.get("ip_rules"))
	@api.doc(parser=parser)
	def delete(self):
		'''ip rules post'''
		args = parser.parse_args()
                log.debug(args)
		return del_ip_rules(args.get("ip_rules"))

