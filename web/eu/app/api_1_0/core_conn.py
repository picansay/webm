#-*-coding:utf-8-*-

import log
from . import api,Resource
from opt_core_conn import get_enable_block,post_enable_block
from opt_core_conn import get_block_prompt,put_block_prompt
from opt_core_conn import get_conn_timeo,put_conn_timeo
from opt_core_conn import get_enable_syn,put_enable_syn
from opt_core_conn import get_enable_udp,put_enable_udp

ns = api.namespace('conn', description='核心操作 API')

parser = api.parser()
parser.add_argument('enable_block', type=str, required=True, help='enable block is 0 or 1', location='form')
@ns.route('/enable_block', endpoint='enable_block')
class EnableBlock(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_block()
	@api.doc(parser=parser)
	def put(self):
		args = parser.parse_args()
                return post_enable_block(args["enable_block"])

syn_parser = api.parser()
syn_parser.add_argument('enable_syn', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_syn', endpoint='enable_syn')
class EnableSyn(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_syn()
	@api.doc(parser=syn_parser)
	def put(self):
		args = syn_parser.parse_args()
                return put_enable_syn(args["enable_syn"])

udp_parser = api.parser()
udp_parser.add_argument('enable_udp', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_udp', endpoint='enable_udp')
class Enableudp(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_udp()
	@api.doc(parser=udp_parser)
	def put(self):
		args = udp_parser.parse_args()
                return put_enable_udp(args["enable_udp"])

timeo_parser = api.parser()
timeo_parser.add_argument('conn_timeo', type=str, required=True, help='1<= conn_timeo <=60', location='form')
@ns.route('/conn_timeo', endpoint='conn_timeo')
class ConnTimeOut(Resource):
	def get(self):
		'''ip filter get'''
		return get_conn_timeo()
	@api.doc(parser=timeo_parser)
	def put(self):
		args = timeo_parser.parse_args()
                return put_conn_timeo(args["conn_timeo"])

prompt_parser = api.parser()
prompt_parser.add_argument('block_prompt', type=str, required=True, help='block prompt', location='form')
@ns.route('/block_prompt', endpoint='block_prompt')
class BlockPrompt(Resource):
	def get(self):
		'''ip filter get'''
		return get_block_prompt()
	@api.doc(parser=prompt_parser)
	def put(self):
		args = prompt_parser.parse_args()
                return put_block_prompt(args["block_prompt"])
