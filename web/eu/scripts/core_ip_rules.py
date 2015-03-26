import log


ip_rules_dic = {}

def write_rule_to_core(rule):
        with open("/proc/knstat/ip_rules", 'w') as f:
                f.write("%s\n" % rule)

def get_ip_rules():
        if()
        return ip_rules_dic

def post_ip_rules(rules):
        lst = ip_rules_dic.get("ip_rules", [])
        log.debug((lst,rules))
        if lst.count(rules):
                log.debug("no rules!")
                return ip_rules_dic
        try:
                write_rule_to_core(rules)
                lst.append(rules)
                log.debug(lst)
                ip_rules_dic["ip_rules"] = lst
        except:
                log.debug("eeeeeeeeee")
                pass
        return ip_rules_dic

def del_ip_rules(rules):
        write_rule_to_core('clear')
        if rules=='clear':
                ip_rules_dic.clear()
                return ip_rules_dic

        lst = ip_rules_dic.get("ip_rules", [])
        lst.remove(rules)
        for ipr in lst:
                write_rule_to_core(ipr)
        ip_rules_dic["ip_rules"] = lst
        return ip_rules_dic


if __name__=="__main__":
        write_rule_to_core("clear")
        write_rule_to_core("192.168.0.1")
        pass
