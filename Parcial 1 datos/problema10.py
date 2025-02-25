# Escribe un programa que verifique si una expresión matemática con paréntesis, 
# corchetes y llaves está bien balanceada usando una pila. 
# Ejemplo: 
# ({[()]}) → Balanceado 
# ({[(])}) → No balanceado 

def esta_balanceada(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'} 

    for caracter in expresion:
        if caracter in "({[":
            pila.append(caracter) 
        elif caracter in ")}]":
            if not pila or pila.pop() != pares[caracter]:
                return False  

    return len(pila) == 0 

expresiones = [
    "({[()]})",  # Balanceado
    "({[(])})",  # No balanceado
    "(([]){})",  # Balanceado
    "([)]",      # No balanceado
    "{[()()]}"   # Balanceado
]

for exp in expresiones:
    resultado = "Balanceado" if esta_balanceada(exp) else "No balanceado"
    print(f"{exp} → {resultado}")
