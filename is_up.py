import os
import re
from sys import argv

def ip_valid(addr: str) -> bool:
    
    ip_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    return bool(ip_pattern.match(addr))




    
def is_up(): 

    subcommand = argv[2]  
    
    if not ip_valid(subcommand):
        print("Adresse IP non valide.")
        exit(3)
    else:
        response = os.system(f"ping -n 1 -w 500 {subcommand} > NUL 2>&1")

        if response == 0:
            print("UP!")
        else:
            print("DOWN!")


    
         

    
    
        
   
    
