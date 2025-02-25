# Se tienen dos conjuntos de números enteros. Escribe un programa que determine 
# si uno es subconjunto del otro.

def verificar_subconjunto(conjunto1, conjunto2):
    if conjunto1.issubset(conjunto2):
        print("El conjunto1 es subconjunto del conjunto2.")
    elif conjunto2.issubset(conjunto1):
        print("El conjunto2 es subconjunto del conjunto1.")
    else:
        print("Ninguno de los conjuntos es subconjunto del otro.")

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("Conjunto A:", A)
print("Conjunto B:", B)
verificar_subconjunto(A, B)



"""
    Determina si uno de los conjuntos es subconjunto del otro.
    
    Args:
        conjunto1 (set): Primer conjunto de números enteros.
        conjunto2 (set): Segundo conjunto de números enteros.
    
    Imprime:
        Un mensaje indicando si conjunto1 es subconjunto de conjunto2,
        o si conjunto2 es subconjunto de conjunto1, o si ninguno lo es.
"""
#issubet() verifica si un conjunto es subconjunto de otro. Devuelve True si es subconjunto, False si no lo es.
#issuperset() verifica si un conjunto es superconjunto de otro. Devuelve True si es superconjunto, False si no lo es.
#set1.issubset(set2) devuelve True si set1 es subconjunto de set2.
#set1.issuperset(set2) devuelve True si set1 es superconjunto de set2.