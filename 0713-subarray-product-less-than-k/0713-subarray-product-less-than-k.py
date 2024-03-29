class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        product_so_far = 1
        subarrays = 0
        total = 0
        left = 0

        for right in range(len(nums)):

            product_so_far *= nums[right]
            subarrays += 1

            while product_so_far >= k and left <= right:
                product_so_far /= nums[left]
                left += 1
                subarrays -= 1

            if product_so_far < k:
                total += subarrays

        return total
        
        
                              
                    
                
            
        