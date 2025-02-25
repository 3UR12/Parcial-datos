# Dado dos conjuntos AAA y BBB, implementa funciones para: 
# • Obtener la unión de ambos conjuntos. 
# • Obtener la intersección de ambos conjuntos. 
# • Obtener la diferencia A−BA - BA−B.

def union_conjuntos(A, B):
    
    #Retorna la unión de los conjuntos A y B.
    return A | B

def interseccion_conjuntos(A, B):
    #Retorna la intersección de los conjuntos A y B.
    return A & B

def diferencia_conjuntos(A, B):
   # Retorna la diferencia A - B (elementos que están en A pero no en B).    
    return A - B

def diferencia_conjuntos_B_A(A, B):   
    #Retorna la diferencia B - A (elementos que están en B pero no en A).
    return B - A

#prueba:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Unión:", union_conjuntos(A, B))
print("Intersección:", interseccion_conjuntos(A, B))
print("Diferencia A - B:", diferencia_conjuntos(A, B))
print("Diferencia B - A:", diferencia_conjuntos_B_A(A, B))
