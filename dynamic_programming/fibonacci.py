import time

# BRUTE FORCE

# start_time = time.time()


# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)


# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(40))


# MEMOIZATION

start_time = time.time()


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))


final_time = time.time()


print(f'Execution Time:\t{(final_time - start_time)}')
