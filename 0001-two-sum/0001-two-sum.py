class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    # initialize an empty dictionary
        num_dict = {}

    # loop through the array
        for i, num in enumerate(nums):

            # calculate the complement
            complement = target - num

            # check if the complement is in the dictionary
            if complement in num_dict:

                # return the indices of the number and its complement
                return [num_dict[complement], i]

            # otherwise, add the number and its index to the dictionary
            else:
                num_dict[num] = i