# Implementa un algoritmo que ordene un arreglo de números enteros utilizando el 
# algoritmo de Ordenamiento por Inserción y determine su complejidad temporal. 

def ordenar_arreglo (lok):
    for i in range(1, len(lok)):
        key = lok[i]
        j = i-1
        while j >=0 and key < lok[j] :
                lok[j + 1] = lok[j]
                j -= 1
        lok[j + 1] = key
    return lok
    
lok = [12, 11, 13, 5, 6]
print ("Arreglo ordenado:")

lok_ordenado = ordenar_arreglo(lok)
print("lok ordenado: ", lok_ordenado)