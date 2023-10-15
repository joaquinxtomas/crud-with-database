import re

def validar_email():
    while True:
        email = input("Introduce tu email: ")
        patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        res = re.match(patron, email)
        if res:
            return email
        else: 
            print("INVALIDO. INTRODUCELO NUEVAMENTE.")