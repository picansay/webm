#-*-coding:utf-8-*-
import log
from . import api,Resource


ns = api.namespace('core/http', description='核心操作 API')


from opt_core_http import get_enable_gzip_uncompress,put_enable_gzip_uncompress
enable_gzip_uncompress_parser = api.parser()
enable_gzip_uncompress_parser.add_argument('enable_gzip_uncompress', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_gzip_uncompress', endpoint='enable_gzip_uncompress')
class Enableenable_gzip_uncompress(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_gzip_uncompress()
	@api.doc(parser=enable_gzip_uncompress_parser)
	def put(self):
		args = enable_gzip_uncompress_parser.parse_args()
                return put_enable_gzip_uncompress(args["enable_gzip_uncompress"])

from opt_core_http import get_domain_cache_max,put_domain_cache_max
domain_cache_max_parser = api.parser()
domain_cache_max_parser.add_argument('domain_cache_max', type=str, required=True, help='0 or 1', location='form')
@ns.route('/domain_cache_max', endpoint='domain_cache_max')
class Enabledomain_cache_max(Resource):
	def get(self):
		'''ip filter get'''
		return get_domain_cache_max()
	@api.doc(parser=domain_cache_max_parser)
	def put(self):
		args = domain_cache_max_parser.parse_args()
                return put_domain_cache_max(args["domain_cache_max"])

from opt_core_http import get_domain_cache_timeo,put_domain_cache_timeo
domain_cache_timeo_parser = api.parser()
domain_cache_timeo_parser.add_argument('domain_cache_timeo', type=str, required=True, help='0 or 1', location='form')
@ns.route('/domain_cache_timeo', endpoint='domain_cache_timeo')
class Enabledomain_cache_timeo(Resource):
	def get(self):
		'''ip filter get'''
		return get_domain_cache_timeo()
	@api.doc(parser=domain_cache_timeo_parser)
	def put(self):
		args = domain_cache_timeo_parser.parse_args()
                return put_domain_cache_timeo(args["domain_cache_timeo"])
from opt_core_http import get_domain_resend_timeo,put_domain_resend_timeo
domain_resend_timeo_parser = api.parser()
domain_resend_timeo_parser.add_argument('domain_resend_timeo', type=str, required=True, help='0 or 1', location='form')
@ns.route('/domain_resend_timeo', endpoint='domain_resend_timeo')
class Enabledomain_resend_timeo(Resource):
	def get(self):
		'''ip filter get'''
		return get_domain_resend_timeo()
	@api.doc(parser=domain_resend_timeo_parser)
	def put(self):
		args = domain_resend_timeo_parser.parse_args()
                return put_domain_resend_timeo(args["domain_resend_timeo"])
from opt_core_http import get_enable_post_scan,put_enable_post_scan
enable_post_scan_parser = api.parser()
enable_post_scan_parser.add_argument('enable_post_scan', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_post_scan', endpoint='enable_post_scan')
class Enableenable_post_scan(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_post_scan()
	@api.doc(parser=enable_post_scan_parser)
	def put(self):
		args = enable_post_scan_parser.parse_args()
                return put_enable_post_scan(args["enable_post_scan"])
from opt_core_http import get_enable_scan_for_trust,put_enable_scan_for_trust
enable_scan_for_trust_parser = api.parser()
enable_scan_for_trust_parser.add_argument('enable_scan_for_trust', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_scan_for_trust', endpoint='enable_scan_for_trust')
class Enableenable_scan_for_trust(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_scan_for_trust()
	@api.doc(parser=enable_scan_for_trust_parser)
	def put(self):
		args = enable_scan_for_trust_parser.parse_args()
                return put_enable_scan_for_trust(args["enable_scan_for_trust"])
from opt_core_http import get_enable_url_scan,put_enable_url_scan
enable_url_scan_parser = api.parser()
enable_url_scan_parser.add_argument('enable_url_scan', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_url_scan', endpoint='enable_url_scan')
class Enableenable_url_scan(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_url_scan()
	@api.doc(parser=enable_url_scan_parser)
	def put(self):
		args = enable_url_scan_parser.parse_args()
                return put_enable_url_scan(args["enable_url_scan"])
from opt_core_http import get_enable_visit_log,put_enable_visit_log
enable_visit_log_parser = api.parser()
enable_visit_log_parser.add_argument('enable_visit_log', type=str, required=True, help='0 or 1', location='form')
@ns.route('/enable_visit_log', endpoint='enable_visit_log')
class Enableenable_visit_log(Resource):
	def get(self):
		'''ip filter get'''
		return get_enable_visit_log()
	@api.doc(parser=enable_visit_log_parser)
	def put(self):
		args = enable_visit_log_parser.parse_args()
                return put_enable_visit_log(args["enable_visit_log"])
from opt_core_http import get_illegal_kw_max_trie_bytes,put_illegal_kw_max_trie_bytes
illegal_kw_max_trie_bytes_parser = api.parser()
illegal_kw_max_trie_bytes_parser.add_argument('illegal_kw_max_trie_bytes', type=str, required=True, help='0 or 1', location='form')
@ns.route('/illegal_kw_max_trie_bytes', endpoint='illegal_kw_max_trie_bytes')
class Enableillegal_kw_max_trie_bytes(Resource):
	def get(self):
		'''ip filter get'''
		return get_illegal_kw_max_trie_bytes()
	@api.doc(parser=illegal_kw_max_trie_bytes_parser)
	def put(self):
		args = illegal_kw_max_trie_bytes_parser.parse_args()
                return put_illegal_kw_max_trie_bytes(args["illegal_kw_max_trie_bytes"])
from opt_core_http import get_illegal_kw_weight,put_illegal_kw_weight
illegal_kw_weight_parser = api.parser()
illegal_kw_weight_parser.add_argument('illegal_kw_weight', type=str, required=True, help='0 or 1', location='form')
@ns.route('/illegal_kw_weight', endpoint='illegal_kw_weight')
class Enableillegal_kw_weight(Resource):
	def get(self):
		'''ip filter get'''
		return get_illegal_kw_weight()
	@api.doc(parser=illegal_kw_weight_parser)
	def put(self):
		args = illegal_kw_weight_parser.parse_args()
                return put_illegal_kw_weight(args["illegal_kw_weight"])
from opt_core_http import get_image_cnt_len_min_bytes,put_image_cnt_len_min_bytes
image_cnt_len_min_bytes_parser = api.parser()
image_cnt_len_min_bytes_parser.add_argument('image_cnt_len_min_bytes', type=str, required=True, help='0 or 1', location='form')
@ns.route('/image_cnt_len_min_bytes', endpoint='image_cnt_len_min_bytes')
class Enableimage_cnt_len_min_bytes(Resource):
	def get(self):
		'''ip filter get'''
		return get_image_cnt_len_min_bytes()
	@api.doc(parser=image_cnt_len_min_bytes_parser)
	def put(self):
		args = image_cnt_len_min_bytes_parser.parse_args()
                return put_image_cnt_len_min_bytes(args["image_cnt_len_min_bytes"])
from opt_core_http import get_inflate_printk_level,put_inflate_printk_level
inflate_printk_level_parser = api.parser()
inflate_printk_level_parser.add_argument('inflate_printk_level', type=str, required=True, help='0 or 1', location='form')
@ns.route('/inflate_printk_level', endpoint='inflate_printk_level')
class Enableinflate_printk_level(Resource):
	def get(self):
		'''ip filter get'''
		return get_inflate_printk_level()
	@api.doc(parser=inflate_printk_level_parser)
	def put(self):
		args = inflate_printk_level_parser.parse_args()
                return put_inflate_printk_level(args["inflate_printk_level"])
from opt_core_http import get_legal_domain_min_200_ok,put_legal_domain_min_200_ok
legal_domain_min_200_ok_parser = api.parser()
legal_domain_min_200_ok_parser.add_argument('legal_domain_min_200_ok', type=str, required=True, help='0 or 1', location='form')
@ns.route('/legal_domain_min_200_ok', endpoint='legal_domain_min_200_ok')
class Enablelegal_domain_min_200_ok(Resource):
	def get(self):
		'''ip filter get'''
		return get_legal_domain_min_200_ok()
	@api.doc(parser=legal_domain_min_200_ok_parser)
	def put(self):
		args = legal_domain_min_200_ok_parser.parse_args()
                return put_legal_domain_min_200_ok(args["legal_domain_min_200_ok"])
from opt_core_http import get_legal_domain_min_req,put_legal_domain_min_req
legal_domain_min_req_parser = api.parser()
legal_domain_min_req_parser.add_argument('legal_domain_min_req', type=str, required=True, help='0 or 1', location='form')
@ns.route('/legal_domain_min_req', endpoint='legal_domain_min_req')
class Enablelegal_domain_min_req(Resource):
	def get(self):
		'''ip filter get'''
		return get_legal_domain_min_req()
	@api.doc(parser=legal_domain_min_req_parser)
	def put(self):
		args = legal_domain_min_req_parser.parse_args()
                return put_legal_domain_min_req(args["legal_domain_min_req"])
from opt_core_http import get_max_kw_per_url,put_max_kw_per_url
max_kw_per_url_parser = api.parser()
max_kw_per_url_parser.add_argument('max_kw_per_url', type=str, required=True, help='0 or 1', location='form')
@ns.route('/max_kw_per_url', endpoint='max_kw_per_url')
class Enablemax_kw_per_url(Resource):
	def get(self):
		'''ip filter get'''
		return get_max_kw_per_url()
	@api.doc(parser=max_kw_per_url_parser)
	def put(self):
		args = max_kw_per_url_parser.parse_args()
                return put_max_kw_per_url(args["max_kw_per_url"])
from opt_core_http import get_url_cache_max,put_url_cache_max
url_cache_max_parser = api.parser()
url_cache_max_parser.add_argument('url_cache_max', type=str, required=True, help='0 or 1', location='form')
@ns.route('/url_cache_max', endpoint='url_cache_max')
class Enableurl_cache_max(Resource):
	def get(self):
		'''ip filter get'''
		return get_url_cache_max()
	@api.doc(parser=url_cache_max_parser)
	def put(self):
		args = url_cache_max_parser.parse_args()
                return put_url_cache_max(args["url_cache_max"])
from opt_core_http import get_url_cache_timeo,put_url_cache_timeo
url_cache_timeo_parser = api.parser()
url_cache_timeo_parser.add_argument('url_cache_timeo', type=str, required=True, help='0 or 1', location='form')
@ns.route('/url_cache_timeo', endpoint='url_cache_timeo')
class Enableurl_cache_timeo(Resource):
	def get(self):
		'''ip filter get'''
		return get_url_cache_timeo()
	@api.doc(parser=url_cache_timeo_parser)
	def put(self):
		args = url_cache_timeo_parser.parse_args()
                return put_url_cache_timeo(args["url_cache_timeo"])
from opt_core_http import get_url_recheck_timeo,put_url_recheck_timeo
url_recheck_timeo_parser = api.parser()
url_recheck_timeo_parser.add_argument('url_recheck_timeo', type=str, required=True, help='0 or 1', location='form')
@ns.route('/url_recheck_timeo', endpoint='url_recheck_timeo')
class Enableurl_recheck_timeo(Resource):
	def get(self):
		'''ip filter get'''
		return get_url_recheck_timeo()
	@api.doc(parser=url_recheck_timeo_parser)
	def put(self):
		args = url_recheck_timeo_parser.parse_args()
                return put_url_recheck_timeo(args["url_recheck_timeo"])

from opt_core_http import get_domain_rules,put_domain_rules
domain_rules_parser = api.parser()
domain_rules_parser.add_argument('domain_rules', type=str, action='append',required=True, help='0 or 1', location='form')
@ns.route('/domain_rules', endpoint='domain_rules')
class Enabledomain_rules(Resource):
	def get(self):
		'''ip filter get'''
		return get_domain_rules()
	@api.doc(parser=domain_rules_parser)
	def post(self):
		args = domain_rules_parser.parse_args()
                log.debug(args)
                return put_domain_rules(args["domain_rules"])
from opt_core_http import get_url_rules,put_url_rules
url_rules_parser = api.parser()
url_rules_parser.add_argument('url_rules', type=str, action='append',required=True, help='0 or 1', location='form')
@ns.route('/url_rules', endpoint='url_rules')
class Enableurl_rules(Resource):
	def get(self):
		'''ip filter get'''
		return get_url_rules()
	@api.doc(parser=url_rules_parser)
	def post(self):
		args = url_rules_parser.parse_args()
                log.debug(args)
                return put_url_rules(args["url_rules"])
#TODO:domain_caches
#TODO:url_caches
#TODO:url_rules
#TODO:illegal_keywords
