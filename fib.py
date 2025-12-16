from functools import lru_cache

@lru_cache(maxsize=100000000)
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
    else:
        return 0
    
if __name__ == '__main__':
    for n in range(1000000):
        print(f"{n}: {fib(n)}")
