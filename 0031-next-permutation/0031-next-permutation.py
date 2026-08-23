class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Find the first decreasing element from the right
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If a larger permutation exists
        if i >= 0:
            # Find the smallest element greater than nums[i]
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the suffix
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1