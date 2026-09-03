class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in results:
                return [results[complement], i]
            results[nums[i]] = i


        return [0, 0]