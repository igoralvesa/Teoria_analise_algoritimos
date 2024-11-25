def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = len(lista) // 2
    left = lista[:pivot]
    right = lista[pivot:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0    
    j = 0 
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result


def kth_smallest_merge_sort(lista, k):
    sorted_list = merge_sort(lista)
    return sorted_list[k - 1]