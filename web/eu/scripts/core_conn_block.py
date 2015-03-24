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

#def write_block_to_proc(enable_block):
#        with open("/proc/knstat/conn/enable_block",'w') as f:
#                f.write("%s\n"%enable_block)


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
