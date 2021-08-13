import time

# BRUTE FORCE

start_time = time.time()


def gridTraversal(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraversal(m-1, n) + gridTraversal(m, n-1)


print(gridTraversal(1, 1))
print(gridTraversal(0, 1))
print(gridTraversal(1, 0))
print(gridTraversal(0, 0))
print(gridTraversal(2, 3))
print(gridTraversal(3, 3))
print(gridTraversal(15, 15))


# MEMOIZATION

# def gridTraversal(m, n, memo={}):
#     key = str(m) + ',' + str(n)

#     if key in memo:
#         return memo[key]
#     if m == 1 and n == 1:
#         return 1
#     if m == 0 or n == 0:
#         return 0
#     memo[key] = gridTraversal(m-1, n, memo) + gridTraversal(m, n-1, memo)
#     return memo[key]


# print(gridTraversal(1, 1))
# print(gridTraversal(0, 1))
# print(gridTraversal(1, 0))
# print(gridTraversal(0, 0))
# print(gridTraversal(2, 3))
# print(gridTraversal(3, 3))
# print(gridTraversal(15, 15))
# print(gridTraversal(50, 50))
# print(gridTraversal(100, 100))


final_time = time.time()


print(f'Execution Time:\t{(final_time - start_time)}')
