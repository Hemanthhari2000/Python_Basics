
# ======================= Problem =======================

'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

'''

# ======================= Test Case =======================
'''
Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''

'''

Follow up: Could you solve it without converting the integer to a string?

'''

# ======================= Solution =======================


def solution(x):
    n = x
    p = 0
    while n > 0:
        rem = n % 10
        p = p*10 + rem
        n = n // 10
    if x == p:
        return True
    else:
        return False
