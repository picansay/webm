import log
import base64

def _write_to_proc(proc, buf, newline=True):
        with open(proc,'w') as f:
                if newline:
                        f.write("%s\n"%buf)
                else:
                        f.write("%s"%buf)
def write_to_proc(proc,buf,newline=True,b64=False):
        try:
                if b64:
                        buf = base64.b64decode(buf) 
                _write_to_proc(proc,buf,newline=newline)
        except:
                raise ValueError
def read_from_proc(proc,newline=False,b64=False):
        buf = ''
        with open(proc,'r') as f:
                buf = f.read()
        
        if not newline:
                if buf and buf.endswith('\n'):
                        buf = buf[0:-1]
        if b64:
                buf = base64.b64encode(buf)
        return buf


def format_retv_msg(func):
        def _format_retv_msg(*args, **kwargs):
                dic = {}
                try:
                        data = func(*args, **kwargs)
                        if data:
                                dic['data'] = data
                        dic['msg'] = "Success"
                        dic['errcode']=0
                except ValueError:
                        pass
                return dic
        return _format_retv_msg
