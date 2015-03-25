import log
from core_utils import write_to_proc,read_from_proc


domain_cache_max_dic={}

def get_domain_cache_max():
        if domain_cache_max_dic:
                return domain_cache_max_dic
        domain_cache_max = read_from_proc("/proc/knstat/http/domain_cache_max")
        domain_cache_max_dic["domain_cache_max"] = domain_cache_max
        return domain_cache_max_dic

def put_domain_cache_max(domain_cache_max):
        log.debug("post enable block")
        if not domain_cache_max_dic:
                get_domain_cache_max()
        if domain_cache_max == domain_cache_max_dic.get("domain_cache_max"):
                return domain_cache_max_dic

        domain_cache_max_dic["domain_cache_max"]=domain_cache_max
        #write_block_to_proc(domain_cache_max)
        write_to_proc("/proc/knstat/http/domain_cache_max", domain_cache_max)
        return domain_cache_max_dic

domain_cache_timeo_dic={}

def get_domain_cache_timeo():
        if domain_cache_timeo_dic:
                return domain_cache_timeo_dic
        domain_cache_timeo = read_from_proc("/proc/knstat/http/domain_cache_timeo")
        domain_cache_timeo_dic["domain_cache_timeo"] = domain_cache_timeo
        return domain_cache_timeo_dic

def put_domain_cache_timeo(domain_cache_timeo):
        log.debug("post enable block")
        if not domain_cache_timeo_dic:
                get_domain_cache_timeo()
        if domain_cache_timeo == domain_cache_timeo_dic.get("domain_cache_timeo"):
                return domain_cache_timeo_dic

        domain_cache_timeo_dic["domain_cache_timeo"]=domain_cache_timeo
        #write_block_to_proc(domain_cache_timeo)
        write_to_proc("/proc/knstat/http/domain_cache_timeo", domain_cache_timeo)
        return domain_cache_timeo_dic

domain_resend_timeo_dic={}

def get_domain_resend_timeo():
        if domain_resend_timeo_dic:
                return domain_resend_timeo_dic
        domain_resend_timeo = read_from_proc("/proc/knstat/http/domain_resend_timeo")
        domain_resend_timeo_dic["domain_resend_timeo"] = domain_resend_timeo
        return domain_resend_timeo_dic

def put_domain_resend_timeo(domain_resend_timeo):
        log.debug("post enable block")
        if not domain_resend_timeo_dic:
                get_domain_resend_timeo()
        if domain_resend_timeo == domain_resend_timeo_dic.get("domain_resend_timeo"):
                return domain_resend_timeo_dic

        domain_resend_timeo_dic["domain_resend_timeo"]=domain_resend_timeo
        #write_block_to_proc(domain_resend_timeo)
        write_to_proc("/proc/knstat/http/domain_resend_timeo", domain_resend_timeo)
        return domain_resend_timeo_dic

enable_post_scan_dic={}

def get_enable_post_scan():
        if enable_post_scan_dic:
                return enable_post_scan_dic
        enable_post_scan = read_from_proc("/proc/knstat/http/enable_post_scan")
        enable_post_scan_dic["enable_post_scan"] = enable_post_scan
        return enable_post_scan_dic

def put_enable_post_scan(enable_post_scan):
        log.debug("post enable block")
        if not enable_post_scan_dic:
                get_enable_post_scan()
        if enable_post_scan == enable_post_scan_dic.get("enable_post_scan"):
                return enable_post_scan_dic

        enable_post_scan_dic["enable_post_scan"]=enable_post_scan
        #write_block_to_proc(enable_post_scan)
        write_to_proc("/proc/knstat/http/enable_post_scan", enable_post_scan)
        return enable_post_scan_dic
enable_scan_for_trust_dic={}

def get_enable_scan_for_trust():
        if enable_scan_for_trust_dic:
                return enable_scan_for_trust_dic
        enable_scan_for_trust = read_from_proc("/proc/knstat/http/enable_scan_for_trust")
        enable_scan_for_trust_dic["enable_scan_for_trust"] = enable_scan_for_trust
        return enable_scan_for_trust_dic

def put_enable_scan_for_trust(enable_scan_for_trust):
        log.debug("post enable block")
        if not enable_scan_for_trust_dic:
                get_enable_scan_for_trust()
        if enable_scan_for_trust == enable_scan_for_trust_dic.get("enable_scan_for_trust"):
                return enable_scan_for_trust_dic

        enable_scan_for_trust_dic["enable_scan_for_trust"]=enable_scan_for_trust
        #write_block_to_proc(enable_scan_for_trust)
        write_to_proc("/proc/knstat/http/enable_scan_for_trust", enable_scan_for_trust)
        return enable_scan_for_trust_dic
enable_url_scan_dic={}

def get_enable_url_scan():
        if enable_url_scan_dic:
                return enable_url_scan_dic
        enable_url_scan = read_from_proc("/proc/knstat/http/enable_url_scan")
        enable_url_scan_dic["enable_url_scan"] = enable_url_scan
        return enable_url_scan_dic

def put_enable_url_scan(enable_url_scan):
        log.debug("post enable block")
        if not enable_url_scan_dic:
                get_enable_url_scan()
        if enable_url_scan == enable_url_scan_dic.get("enable_url_scan"):
                return enable_url_scan_dic

        enable_url_scan_dic["enable_url_scan"]=enable_url_scan
        #write_block_to_proc(enable_url_scan)
        write_to_proc("/proc/knstat/http/enable_url_scan", enable_url_scan)
        return enable_url_scan_dic
enable_visit_log_dic={}

def get_enable_visit_log():
        if enable_visit_log_dic:
                return enable_visit_log_dic
        enable_visit_log = read_from_proc("/proc/knstat/http/enable_visit_log")
        enable_visit_log_dic["enable_visit_log"] = enable_visit_log
        return enable_visit_log_dic

def put_enable_visit_log(enable_visit_log):
        log.debug("post enable block")
        if not enable_visit_log_dic:
                get_enable_visit_log()
        if enable_visit_log == enable_visit_log_dic.get("enable_visit_log"):
                return enable_visit_log_dic

        enable_visit_log_dic["enable_visit_log"]=enable_visit_log
        #write_block_to_proc(enable_visit_log)
        write_to_proc("/proc/knstat/http/enable_visit_log", enable_visit_log)
        return enable_visit_log_dic
illegal_kw_max_trie_bytes_dic={}

def get_illegal_kw_max_trie_bytes():
        if illegal_kw_max_trie_bytes_dic:
                return illegal_kw_max_trie_bytes_dic
        illegal_kw_max_trie_bytes = read_from_proc("/proc/knstat/http/illegal_kw_max_trie_bytes")
        illegal_kw_max_trie_bytes_dic["illegal_kw_max_trie_bytes"] = illegal_kw_max_trie_bytes
        return illegal_kw_max_trie_bytes_dic

def put_illegal_kw_max_trie_bytes(illegal_kw_max_trie_bytes):
        log.debug("post enable block")
        if not illegal_kw_max_trie_bytes_dic:
                get_illegal_kw_max_trie_bytes()
        if illegal_kw_max_trie_bytes == illegal_kw_max_trie_bytes_dic.get("illegal_kw_max_trie_bytes"):
                return illegal_kw_max_trie_bytes_dic

        illegal_kw_max_trie_bytes_dic["illegal_kw_max_trie_bytes"]=illegal_kw_max_trie_bytes
        #write_block_to_proc(illegal_kw_max_trie_bytes)
        write_to_proc("/proc/knstat/http/illegal_kw_max_trie_bytes", illegal_kw_max_trie_bytes)
        return illegal_kw_max_trie_bytes_dic

enable_gzip_uncompress_dic={}

def get_enable_gzip_uncompress():
        if enable_gzip_uncompress_dic:
                return enable_gzip_uncompress_dic
        enable_gzip_uncompress = read_from_proc("/proc/knstat/http/enable_gzip_uncompress")
        enable_gzip_uncompress_dic["enable_gzip_uncompress"] = enable_gzip_uncompress
        return enable_gzip_uncompress_dic

def put_enable_gzip_uncompress(enable_gzip_uncompress):
        log.debug("post enable block")
        if not enable_gzip_uncompress_dic:
                get_enable_gzip_uncompress()
        if enable_gzip_uncompress == enable_gzip_uncompress_dic.get("enable_gzip_uncompress"):
                return enable_gzip_uncompress_dic

        enable_gzip_uncompress_dic["enable_gzip_uncompress"]=enable_gzip_uncompress
        #write_block_to_proc(enable_gzip_uncompress)
        write_to_proc("/proc/knstat/http/enable_gzip_uncompress", enable_gzip_uncompress)
        return enable_gzip_uncompress_dic
illegal_kw_weight_dic={}

def get_illegal_kw_weight():
        if illegal_kw_weight_dic:
                return illegal_kw_weight_dic
        illegal_kw_weight = read_from_proc("/proc/knstat/http/illegal_kw_weight")
        illegal_kw_weight_dic["illegal_kw_weight"] = illegal_kw_weight
        return illegal_kw_weight_dic

def put_illegal_kw_weight(illegal_kw_weight):
        log.debug("post enable block")
        if not illegal_kw_weight_dic:
                get_illegal_kw_weight()
        if illegal_kw_weight == illegal_kw_weight_dic.get("illegal_kw_weight"):
                return illegal_kw_weight_dic

        illegal_kw_weight_dic["illegal_kw_weight"]=illegal_kw_weight
        #write_block_to_proc(illegal_kw_weight)
        write_to_proc("/proc/knstat/http/illegal_kw_weight", illegal_kw_weight)
        return illegal_kw_weight_dic
image_cnt_len_min_bytes_dic={}

def get_image_cnt_len_min_bytes():
        if image_cnt_len_min_bytes_dic:
                return image_cnt_len_min_bytes_dic
        image_cnt_len_min_bytes = read_from_proc("/proc/knstat/http/image_cnt_len_min_bytes")
        image_cnt_len_min_bytes_dic["image_cnt_len_min_bytes"] = image_cnt_len_min_bytes
        return image_cnt_len_min_bytes_dic

def put_image_cnt_len_min_bytes(image_cnt_len_min_bytes):
        log.debug("post enable block")
        if not image_cnt_len_min_bytes_dic:
                get_image_cnt_len_min_bytes()
        if image_cnt_len_min_bytes == image_cnt_len_min_bytes_dic.get("image_cnt_len_min_bytes"):
                return image_cnt_len_min_bytes_dic

        image_cnt_len_min_bytes_dic["image_cnt_len_min_bytes"]=image_cnt_len_min_bytes
        #write_block_to_proc(image_cnt_len_min_bytes)
        write_to_proc("/proc/knstat/http/image_cnt_len_min_bytes", image_cnt_len_min_bytes)
        return image_cnt_len_min_bytes_dic
inflate_printk_level_dic={}

def get_inflate_printk_level():
        if inflate_printk_level_dic:
                return inflate_printk_level_dic
        inflate_printk_level = read_from_proc("/proc/knstat/http/inflate_printk_level")
        inflate_printk_level_dic["inflate_printk_level"] = inflate_printk_level
        return inflate_printk_level_dic

def put_inflate_printk_level(inflate_printk_level):
        log.debug("post enable block")
        if not inflate_printk_level_dic:
                get_inflate_printk_level()
        if inflate_printk_level == inflate_printk_level_dic.get("inflate_printk_level"):
                return inflate_printk_level_dic

        inflate_printk_level_dic["inflate_printk_level"]=inflate_printk_level
        #write_block_to_proc(inflate_printk_level)
        write_to_proc("/proc/knstat/http/inflate_printk_level", inflate_printk_level)
        return inflate_printk_level_dic
legal_domain_min_200_ok_dic={}

def get_legal_domain_min_200_ok():
        if legal_domain_min_200_ok_dic:
                return legal_domain_min_200_ok_dic
        legal_domain_min_200_ok = read_from_proc("/proc/knstat/http/legal_domain_min_200_ok")
        legal_domain_min_200_ok_dic["legal_domain_min_200_ok"] = legal_domain_min_200_ok
        return legal_domain_min_200_ok_dic

def put_legal_domain_min_200_ok(legal_domain_min_200_ok):
        log.debug("post enable block")
        if not legal_domain_min_200_ok_dic:
                get_legal_domain_min_200_ok()
        if legal_domain_min_200_ok == legal_domain_min_200_ok_dic.get("legal_domain_min_200_ok"):
                return legal_domain_min_200_ok_dic

        legal_domain_min_200_ok_dic["legal_domain_min_200_ok"]=legal_domain_min_200_ok
        #write_block_to_proc(legal_domain_min_200_ok)
        write_to_proc("/proc/knstat/http/legal_domain_min_200_ok", legal_domain_min_200_ok)
        return legal_domain_min_200_ok_dic
legal_domain_min_req_dic={}

def get_legal_domain_min_req():
        if legal_domain_min_req_dic:
                return legal_domain_min_req_dic
        legal_domain_min_req = read_from_proc("/proc/knstat/http/legal_domain_min_req")
        legal_domain_min_req_dic["legal_domain_min_req"] = legal_domain_min_req
        return legal_domain_min_req_dic

def put_legal_domain_min_req(legal_domain_min_req):
        log.debug("post enable block")
        if not legal_domain_min_req_dic:
                get_legal_domain_min_req()
        if legal_domain_min_req == legal_domain_min_req_dic.get("legal_domain_min_req"):
                return legal_domain_min_req_dic

        legal_domain_min_req_dic["legal_domain_min_req"]=legal_domain_min_req
        #write_block_to_proc(legal_domain_min_req)
        write_to_proc("/proc/knstat/http/legal_domain_min_req", legal_domain_min_req)
        return legal_domain_min_req_dic
max_kw_per_url_dic={}

def get_max_kw_per_url():
        if max_kw_per_url_dic:
                return max_kw_per_url_dic
        max_kw_per_url = read_from_proc("/proc/knstat/http/max_kw_per_url")
        max_kw_per_url_dic["max_kw_per_url"] = max_kw_per_url
        return max_kw_per_url_dic

def put_max_kw_per_url(max_kw_per_url):
        log.debug("post enable block")
        if not max_kw_per_url_dic:
                get_max_kw_per_url()
        if max_kw_per_url == max_kw_per_url_dic.get("max_kw_per_url"):
                return max_kw_per_url_dic

        max_kw_per_url_dic["max_kw_per_url"]=max_kw_per_url
        #write_block_to_proc(max_kw_per_url)
        write_to_proc("/proc/knstat/http/max_kw_per_url", max_kw_per_url)
        return max_kw_per_url_dic
url_cache_max_dic={}

def get_url_cache_max():
        if url_cache_max_dic:
                return url_cache_max_dic
        url_cache_max = read_from_proc("/proc/knstat/http/url_cache_max")
        url_cache_max_dic["url_cache_max"] = url_cache_max
        return url_cache_max_dic

def put_url_cache_max(url_cache_max):
        log.debug("post enable block")
        if not url_cache_max_dic:
                get_url_cache_max()
        if url_cache_max == url_cache_max_dic.get("url_cache_max"):
                return url_cache_max_dic

        url_cache_max_dic["url_cache_max"]=url_cache_max
        #write_block_to_proc(url_cache_max)
        write_to_proc("/proc/knstat/http/url_cache_max", url_cache_max)
        return url_cache_max_dic
url_cache_timeo_dic={}

def get_url_cache_timeo():
        if url_cache_timeo_dic:
                return url_cache_timeo_dic
        url_cache_timeo = read_from_proc("/proc/knstat/http/url_cache_timeo")
        url_cache_timeo_dic["url_cache_timeo"] = url_cache_timeo
        return url_cache_timeo_dic

def put_url_cache_timeo(url_cache_timeo):
        log.debug("post enable block")
        if not url_cache_timeo_dic:
                get_url_cache_timeo()
        if url_cache_timeo == url_cache_timeo_dic.get("url_cache_timeo"):
                return url_cache_timeo_dic

        url_cache_timeo_dic["url_cache_timeo"]=url_cache_timeo
        #write_block_to_proc(url_cache_timeo)
        write_to_proc("/proc/knstat/http/url_cache_timeo", url_cache_timeo)
        return url_cache_timeo_dic
url_recheck_timeo_dic={}

def get_url_recheck_timeo():
        if url_recheck_timeo_dic:
                return url_recheck_timeo_dic
        url_recheck_timeo = read_from_proc("/proc/knstat/http/url_recheck_timeo")
        url_recheck_timeo_dic["url_recheck_timeo"] = url_recheck_timeo
        return url_recheck_timeo_dic

def put_url_recheck_timeo(url_recheck_timeo):
        log.debug("post enable block")
        if not url_recheck_timeo_dic:
                get_url_recheck_timeo()
        if url_recheck_timeo == url_recheck_timeo_dic.get("url_recheck_timeo"):
                return url_recheck_timeo_dic

        url_recheck_timeo_dic["url_recheck_timeo"]=url_recheck_timeo
        #write_block_to_proc(url_recheck_timeo)
        write_to_proc("/proc/knstat/http/url_recheck_timeo", url_recheck_timeo)
        return url_recheck_timeo_dic

domain_rules_dic={}

def get_domain_rules():
        if domain_rules_dic:
                return domain_rules_dic
        #rules = read_from_proc("/proc/knstat/http/domain_rules",newline=True)
        rules = open("/proc/knstat/http/domain_rules").readlines()
        log.debug(rules)
        for rule in rules:
                log.debug(rule)
                opt,domain=rule.split(' ')
                if domain.endswith('\n'):
                        domain = domain[0:-1]
                domain_rules_dic[domain]=opt
                
        #domain_rules_dic["domain_rules"] = domain_rules
        return domain_rules_dic

def put_domain_rules(domain_rules):
        if not domain_rules_dic:
                get_domain_rules()
        if domain_rules == domain_rules_dic.get("domain_rules"):
                return domain_rules_dic

        #write_block_to_proc(domain_rules)
        log.debug(domain_rules)
        for rule in domain_rules:
                log.debug(rule)
                opt,domain=rule.split(' ')
                if opt=='-':
                        if domain_rules_dic.has_key(domain):
                                write_to_proc("/proc/knstat/http/domain_rules",rule) 
                                del domain_rules_dic[domain]
                else:
                        write_to_proc("/proc/knstat/http/domain_rules",rule) 
                        domain_rules_dic[domain]=opt
        return domain_rules_dic
#TODO:domain_rule
#TODO:domain_cache
#TODO:url_rule
#TODO:url_cache
#TODO:illegal_keywords
