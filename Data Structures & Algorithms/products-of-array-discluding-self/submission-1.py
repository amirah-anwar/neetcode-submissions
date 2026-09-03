class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_without_0 = 1
        zeros_count = 0
        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                product_without_0 *= num
            product *= num
            

        result = []

        for num in nums:
            if num == 0:
                result.append(int(product_without_0) if zeros_count == 1 else 0)
            else:
                result.append(int(product / num))
        
        return result