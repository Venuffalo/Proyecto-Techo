# Ejercicio: Hace una funcion en Python que reciba una lista de numeros y la devuelva ordenada de menor a mayor. Probala con la lista [5, 2, 9, 1, 7] y mostra el resultado.
# Generado y probado por Profesor de Codigo el 2026-11-24 02:03:48

def sort_list(numbers):
    return sorted(numbers)

# Test the function with the provided list
test_list = [5, 2, 9, 1, 7]
sorted_list = sort_list(test_list)
print(sorted_list)
