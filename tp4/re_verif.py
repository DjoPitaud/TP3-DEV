import re

def verifier_msg(msg):
    
    pattern = r"(waf|meo)"
    
    return bool(re.search(pattern, msg))


