# ======================= Problem =======================

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit
# integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers
# (signed or unsigned).


# ======================= Test Case =======================

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21

# Input: x = 0
# Output: 0


# ======================= Solution =======================


class Solution:
    def reverseDigits(self, x: int) -> int:
        b = 0
        while x > 0:
            r = x % 10
            b = b * 10 + r
            x = x // 10
        return b

    def reverse(self, x: int) -> int:
        rev = self.reverseDigits(x) if x >= 0 else -self.reverseDigits(-x)
        if rev not in range(-2**31, 2**31):
            return 0
        else:
            return rev


x = -321

sol = Solution()

val = sol.reverse(x)


print(f"Approach\t|\tSolution\t|\tRuntime\t|\tMemory")
print(f"General \t|\t{val}   \t|\t32ms   \t|\t14MB")
