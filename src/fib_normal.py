from functools import cache


@cache
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be smaller than 0!")
    return n if n == 0 or n == 1 else fib(n-1) + fib(n-2)

print(fib(n=500))