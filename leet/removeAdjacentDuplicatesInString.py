# ======================= Problem =======================

# You are given a string s consisting of lowercase English letters. 
# A duplicate removal consists of choosing two adjacent and equal letters 
# and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.
# It can be proven that the answer is unique.

# ======================= Test Case =======================

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are 
# adjacent and equal, and this is the only possible move.  The result of this 
# move is that the string is "aaca", of which only "aa" is possible, so the 
# final string is "ca".

# ======================= Solution =======================
class Solution:
    def __init__(self) -> None:
        self.stack = []

    def removeDuplicates(self, s: str) -> str:
        for letter in s:
            if len(self.stack) == 0 or letter != self.stack[-1]:
                self.stack.append(letter)
            else:
                self.stack.pop()
        return ''.join(self.stack)

solution = Solution()
sol = solution.removeDuplicates('hehhehe')
print(sol)