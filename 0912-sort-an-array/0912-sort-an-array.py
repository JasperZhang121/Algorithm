class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # merge sort + two pointers
        
    #                   Divide                    Merge
    #               5   2   3   1              1   2   3   5
    #                   /   \                                   -> Three pointers (one pointer in [2,5] one pointer in [1,3], one pointer in [1,2,3,5] 
    #               5   2   3   1                |      |
    #                /\       /\                2 5    1 3 
    #               5  2     3  1   
        
        
        def merge(arr,l,m,r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i,j,k = l,0,0
            
            while j<len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1
            
            while j < len(left):
                nums[i] = left[j]
                i+=1
                j+=1
                
            while k<len(right):
                nums[i] = right[k]
                i+=1
                k+=1
                
        
        def mergeSort(arr,l,r):
            
            if l==r: return arr
            
            m = (l+r)//2
            
            # divide until base case
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            
            # merge subarrays 
            merge(arr,l,m,r)
            return arr
        
        return mergeSort(nums,0,len(nums)-1)
    
    