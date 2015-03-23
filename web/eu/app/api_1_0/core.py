from . import api,Resource
#-*-coding:utf-8-*-


ns = api.namespace('core', description='核心操作 API')


ip_filter_dic={}

parser = api.parser()
parser.add_argument('ip_ranger', type=str, required=True, help='IP范围', location='form')

@ns.route('/ipfilter/', endpoint='ipfilter')
class IpFilter(Resource):
	def get(self):
		'''ip filter get'''
		return ip_filter_dic
	@api.doc(parser=parser)
	def post(self):
		'''ip filter post'''
		args = parser.parse_args()
		print args
		ip_ranger_lst = ip_filter_dic.get("ip_filter", [])
		ip_ranger_lst.append(args.get("ip_ranger",None))
		ip_filter_dic["ip_filter"]=ip_ranger_lst
		return ip_filter_dic
