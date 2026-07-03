class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dictionary:
                return [dictionary[complement], i]

            dictionary[nums[i]] = i

nums = [2, 7, 11, 15]
target = 13
solution = Solution()
result = solution.twoSum(nums, target)
print(result)
