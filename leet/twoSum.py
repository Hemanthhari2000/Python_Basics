# ======================= Problem =======================

# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.


# ======================= Test Case =======================

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# ======================= Solution =======================

from typing import List


class Solution:
    def twoSumGeneralApproach(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumAdvancedApproach(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for count, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], count]
            lookup[num] = count


nums = [2, 7, 11, 15]
target = 22

sol = Solution()

sol1 = sol.twoSumGeneralApproach(nums, target)
sol2 = sol.twoSumAdvancedApproach(nums, target)

print(f"Approach\t|\tSolution\t|\tRuntime\t|\tMemory")
print(f"General \t|\t{sol1}  \t|\t4000ms \t|\t14MB")
print(f"Advanced\t|\t{sol2}  \t|\t52ms   \t|\t15MB")
