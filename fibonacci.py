import time
from functools import lru_cache,cache


class Fibonacci:

    def __init__(self):
        self.cache = {0:0, 1:1}
    def calcola_elemento(self, n):
        if n==0:
            return 0
        elif n ==1:
            return 1
        else:
           return self.calcola_elemento(n-1)+self.calcola_elemento(n-2)


    def calcola_elemento_cache(self, n):
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = self.calcola_elemento_cache(n-1)+self.calcola_elemento_cache(n-2)
            return self.cache[n]

    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento_lru(n - 1) + self.calcola_elemento_lru(n - 2)

if __name__ == '__main__':
    fib = Fibonacci()
    N = 20
    start = time.time()
    elem = fib.calcola_elemento(N)
    end = time.time()
    print(f"L'elemento {N} della sequenza è {elem}")
    print(f"Ci ha impiegato {end-start} secondi")

    start = time.time()
    elem = fib.calcola_elemento_cache(N)
    end = time.time()
    print(f"L'elemento {N} della sequenza è {elem}")
    print(f"Ci ha impiegato {end - start} secondi con cache")

    start = time.time()
    elem = fib.calcola_elemento_lru(N)
    end = time.time()
    print(f"L'elemento {N} della sequenza è {elem}")
    print(f"Ci ha impiegato {end - start} secondi con lru")