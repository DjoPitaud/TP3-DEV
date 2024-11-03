import re

def integer(n_str):
    
    if re.fullmatch(r"-?\d+", n_str):
      
        n = int(n_str)
        if -100000 <= n <= 100000: 
            return True
    return False