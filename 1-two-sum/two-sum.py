class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_list = []
        for idx1 in range(0, len(nums)):
            for idx2 in range(idx1 +1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    answer_list.append(idx1)
                    answer_list.append(idx2)
                    return answer_list
