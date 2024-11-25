import insertion_sort
import merge_sort

import random
import time
import numpy as np

sizes = [100, 200, 500, 1000, 1500, 2000, 3000, 4000, 5000, 10000]
k = 50
reps = 10

insertion_results = []
merge_results = []

def get_list(size):
    return random.sample(range(size * 10), size)


#Testar resultados

for size in sizes:
    insertion_times = []
    merge_times = []

    for _ in range(reps):
        lista = get_list(size)
        
        lista_insertion = lista.copy()
        lista_merge = lista.copy()
        
        #Medir o tempo pro Insertion sort
        start_time = time.time()
        insertion_sort.kth_smallest_sort(lista_insertion, k)
        end_time = time.time()
        insertion_times.append(end_time - start_time)
        
        #Medir o tempo pro Merge sort
        start_time = time.time()
        merge_sort.kth_smallest_merge_sort(lista_merge, k)
        end_time = time.time()
        merge_times.append(end_time - start_time)
        
    #Calcular tempo médio e tempo máximo pro Insertion sort
    avg_time_insertion = np.mean(insertion_times)
    max_time_insertion = np.max(insertion_times)
    insertion_results.append({
        'size': size,
        'avg_time': avg_time_insertion,
        'max_time': max_time_insertion
        })
    
    #Calcular tempo médio e tempo máximo pro Merge sort
    avg_time_merge = np.mean(merge_times)
    max_time_merge = np.max(merge_times)
    merge_results.append({
        'size': size,
        'avg_time': avg_time_merge,
        'max_time': max_time_merge
        })
    
#Printar resultados do Merge sort
print("Tempos do Merge Sort:")
for result in merge_results:
    size = result['size']
    avg_time_merge = result['avg_time']
    max_time_merge = result['max_time']
    print(f"Tamanho: {size}, Tempo Médio: {avg_time_merge:.6f}s, Tempo Máximo: {max_time_merge:.6f}s")
    
    
print()
print()

#Printar resultados do Insertion sort
print("Tempos do Insertion Sort:")
for result in insertion_results:
    size = result['size']
    avg_time_insertion = result['avg_time']
    max_time_insertion = result['max_time']
    print(f"Tamanho: {size}, Tempo Médio: {avg_time_insertion:.6f}s, Tempo Máximo: {max_time_insertion:.6f}s")
    