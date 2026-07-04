class Solutions(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write_index = 1

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index
    

nums = [1, 1, 2, 2, 3, 4, 4, 5,8,8,8,9,9,9]
solution = Solutions()
new_length = solution.removeDuplicates(nums)

print("New length:", new_length)
print("Modified array:", nums[:new_length])
