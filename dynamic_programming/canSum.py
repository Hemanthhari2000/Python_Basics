import time

# BRUTE FORCE

start_time = time.time()


# def canSum(targetSum, numbers):
#     if targetSum == 0:
#         return True
#     if targetSum < 0:
#         return False

#     for num in numbers:
#         rem = targetSum - num
#         if canSum(rem, numbers):
#             return True

#     return False


# print(canSum(7, [2, 3]))
# print(canSum(7, [5, 3, 4, 7]))
# print(canSum(7, [2, 4]))
# print(canSum(8, [2, 3, 5]))
# print(canSum(250, [7, 14]))


# MEMOIZATION


def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        rem = targetSum - num
        if canSum(rem, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return memo[targetSum]


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))


final_time = time.time()


print(f'Execution Time:\t{(final_time - start_time)}')
