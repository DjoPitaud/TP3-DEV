def port_valid(n):
    
    if isinstance(n, int):
        
        if 0 <= n <= 65535:
            return True
    return False

def port_private(n):
    
    if isinstance(n, int):
        
        if 0 <= n <= 1024:
            return False
    return True
