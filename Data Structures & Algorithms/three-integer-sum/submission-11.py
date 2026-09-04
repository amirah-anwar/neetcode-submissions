class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = []
       
        for i, a in enumerate(sorted_nums):
            if a > 0:
                break

            if i > 0 and a == sorted_nums[i - 1]:
                continue
            j = i+1
            k = len(sorted_nums) - 1
            triplet = []
            while j < k:
                total = a + sorted_nums[j] + sorted_nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    triplet = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    triplets.append(triplet)
                    j += 1
                    k -= 1


                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1


                

        return triplets