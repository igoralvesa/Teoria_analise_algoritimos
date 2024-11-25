def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = key

def kth_smallest_sort(lista, k):
    # Sort the array using insertion sort
    insertion_sort(lista)
    # Return the k-th smallest element (0-based index)
    return lista[k - 1]