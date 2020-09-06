from typing import Generator
from typing import Dict

# using generators. Use for loop in main to access all elements
def fib(n: int) -> Generator[int, None, None]:
    yield 0 
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

# using memoization
def fib_memo(n: int) -> int:
    memo: Dict[int, int] = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

if __name__ == "__main__":
    print(fib_memo(50))