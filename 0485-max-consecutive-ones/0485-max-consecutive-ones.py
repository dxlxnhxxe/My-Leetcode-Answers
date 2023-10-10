class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         count = max_count = 0
         for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Reset count of 1's to zero.
                count = 0
            # Update maximum count of consecutive 1's.
            max_count = max(max_count, count)
         return max_count