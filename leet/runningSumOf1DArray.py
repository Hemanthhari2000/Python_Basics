# ======================= Problem =======================

'''
Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

'''

# ======================= Test Case =======================
'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

'''

# ======================= Solution =======================

from typing import List
class Solution:

    @staticmethod
    def runningSum(nums: List[int]) -> List[int]:
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]


nums = [1, 2, 3, 4, 5]
sol = Solution.runningSum(nums)
print(sol)
