
# ======================= Problem =======================

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


'''

# ======================= Test Case =======================
'''

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

# ======================= Solution =======================


def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    lookup = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in s:
        if c in lookup.keys():
            stack.append(c)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if c != lookup[a]:
                return False
    return stack == []
