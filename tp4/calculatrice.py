from ast import literal_eval
from operator import add, sub, mul, truediv

from verif_integer import integer


OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

def calculatrice(request):


    if isinstance(request, str):
        
        parts = request.split()
        
        if len(parts) == 3:
            if integer(parts[0]) == True:
                if integer(parts[2]) == True:
                    try:
                        
                        left = literal_eval(parts[0])
                        operator_symbol = parts[1]
                        right = literal_eval(parts[2])
                        
                        
                        if operator_symbol in OPERATIONS:
                            result = OPERATIONS[operator_symbol](left, right)
                            return result
                        else:
                            raise ValueError("Opérateur non supporté.")
                    except (ValueError, ZeroDivisionError) as e:
                        print(f"Erreur : {e}")
                else:
                    print("Le deuxième nombre doit être compris entre -100000 et 100000.")
            else:
                print("Le premier nombre doit être compris entre -100000 et 100000.")
        else:
            print("Expression invalide. Veuillez utiliser le format 'nombre(entre -100000 et 100000) opérateur( +, -, *, /) nombre(entre -100000 et 100000)'.")
    else:
        raise TypeError("Nice try vilain hacker.")
   

