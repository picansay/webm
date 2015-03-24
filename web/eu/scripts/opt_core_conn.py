import log

def write_to_proc(proc, buf):
        with open(proc,'w') as f:
                f.write("%s\n"%buf)
def read_from_proc(proc):
        buf = ''
        with open(proc,'r') as f:
                buf = f.read()
        
        if buf and buf.endswith('\n'):
                buf = buf[0:-1]
        return buf

enable_block_dic={}

def get_enable_block():
        if enable_block_dic:
                return enable_block_dic
        enable_block = read_from_proc("/proc/knstat/conn/enable_block")
        enable_block_dic["enable_block"] = enable_block
        return enable_block_dic

def post_enable_block(enable_block):
        log.debug("post enable block")
        if not enable_block_dic:
                get_enable_block()
        if enable_block == enable_block_dic.get("enable_block"):
                return enable_block_dic

        enable_block_dic["enable_block"]=enable_block
        #write_block_to_proc(enable_block)
        write_to_proc("/proc/knstat/conn/enable_block", enable_block)
        return enable_block_dic

enable_syn_dic={}

def get_enable_syn():
        if enable_syn_dic:
                return enable_syn_dic
        enable_syn = read_from_proc("/proc/knstat/conn/syn_start_tcp_ss")
        enable_syn_dic["enable_syn"] = enable_syn
        return enable_syn_dic

def put_enable_syn(enable_syn):
        log.debug("post enable syn")
        if not enable_syn_dic:
                get_enable_syn()
        if enable_syn == enable_syn_dic.get("enable_syn"):
                return enable_syn_dic

        enable_syn_dic["enable_syn"]=enable_syn
        #write_syn_to_proc(enable_syn)
        write_to_proc("/proc/knstat/conn/syn_start_tcp_ss", enable_syn)
        return enable_syn_dic

enable_udp_dic={}

def get_enable_udp():
        if enable_udp_dic:
                return enable_udp_dic
        enable_udp = read_from_proc("/proc/knstat/conn/enable_udp")
        enable_udp_dic["enable_udp"] = enable_udp
        return enable_udp_dic

def put_enable_udp(enable_udp):
        log.debug("post enable udp")
        if not enable_udp_dic:
                get_enable_udp()
        if enable_udp == enable_udp_dic.get("enable_udp"):
                return enable_udp_dic

        enable_udp_dic["enable_udp"]=enable_udp
        #write_udp_to_proc(enable_udp)
        write_to_proc("/proc/knstat/conn/enable_udp", enable_udp)
        return enable_udp_dic

conn_timeo_dic={}

#def write_block_to_proc(enable_block):
#        with open("/proc/knstat/conn/enable_block",'w') as f:
#                f.write("%s\n"%enable_block)


def get_conn_timeo():
        if conn_timeo_dic:
                return conn_timeo_dic
        conn_timeo = read_from_proc("/proc/knstat/conn/conn_timeo")
        conn_timeo_dic["conn_timeo"] = conn_timeo
        return conn_timeo_dic 

def put_conn_timeo(conn_timeo):
        if not conn_timeo_dic:
                get_conn_timeo()
        if conn_timeo == conn_timeo_dic.get("conn_timeo"):
                return conn_timeo_dic

        conn_timeo_dic["conn_timeo"]=conn_timeo
        #write_block_to_proc(enable_block)
        write_to_proc("/proc/knstat/conn/conn_timeo", conn_timeo)
        return conn_timeo_dic
block_prompt_dic={}


def get_block_prompt():
        if block_prompt_dic:
                return block_prompt_dic
        prompt = read_from_proc('/proc/knstat/conn/block_prompt')
        if prompt:
                block_prompt_dic['block_prompt'] = prompt
        return block_prompt_dic

def put_block_prompt(prompt):
        if not enable_block_dic:
                get_block_prompt()
        
        if prompt == block_prompt_dic.get("block_prompt"):
                return block_prompt_dic
        block_prompt_dic["block_prompt"]=prompt
        write_to_proc("/proc/knstat/conn/block_prompt",prompt)
        return block_prompt_dic
