
# ======================= Problem =======================

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

'''

# ======================= Test Case =======================
'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

# ======================= Solution =======================


def solution(strs):
    prefix = strs[0]
    for word in strs[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


solution(["flower", "flow", "flight"])
