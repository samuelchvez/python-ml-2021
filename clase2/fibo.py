'''
Pure functions:
1. Dependen unicamente de los parametros
2. No tienen random
3. No tienen efectos colaterales

Las funciones puras son memoizables
'''
import time

def fibo(n):
    if n < 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)

cache = {}
def fibo_cache(n):
    if n in cache:
        return cache[n]

    if n < 2:
        cache[n] = 1
        return 1

    cache[n] = fibo_cache(n - 1) + fibo_cache(n - 2)
    return cache[n]



FIBO_TERM = 35

start = time.time()
print(fibo(FIBO_TERM))
print('Computed in: ', time.time() - start)

start = time.time()
print(fibo_cache(FIBO_TERM))
print('Computed in: ', time.time() - start)
