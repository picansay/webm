
version_dic = {}

def get_core_version():
        if version_dic:
                return version_dic
        with open("/proc/knstat/version",'r') as f:
                version=f.read()
        if version.endswith("\n"):
                version = version[0:-1]
        version_dic["version"] = version
        return version_dic

if __name__ == "__main__":
        print get_core_version()
