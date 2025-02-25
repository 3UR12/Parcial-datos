# Dado un arreglo de enteros de tamaño NNN, escribir una función que encuentre 
# el subarreglo con la suma más grande y devuelva dicha suma.
su = 0
csu = 0
def encontrar_arreglo_mayor(arr):
    max_sum = su
    current_sum = csu
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


print(encontrar_arreglo_mayor([-2, 1, -3, 4, -1, 2, 1, -5, 4])) 