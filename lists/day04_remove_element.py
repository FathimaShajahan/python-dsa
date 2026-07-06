class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Input array
nums = list(map(int, input("Enter array elements separated by space: ").split()))

# Value to remove
val = int(input("Enter value to remove: "))

# Create object
solution = Solution()

# Call function
k = solution.removeElement(nums, val)

# Output
print("\nNumber of elements after removal:", k)
print("Updated array:", nums[:k])