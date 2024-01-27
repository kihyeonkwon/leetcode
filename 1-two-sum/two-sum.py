class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Dictionary to store numbers and their indices

        for idx, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_dict:
                return [num_dict[complement], idx]

            # Add the current number and its index to the dictionary
            num_dict[num] = idx

        # If no solution is found, return an empty list
        return []
