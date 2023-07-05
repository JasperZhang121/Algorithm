class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        
        // SlideWindow
        // Fast pointer will go until it reach the max zero limit
        // Then, the slow pointer will move towards faster pointer and calculate max length untill the max zero limit is removed by reducing it whenver the slow pointer is 0 and going to move right.
        
        int i = 0, res = 0, n = nums.size(), zeros = 0;
        
        for (int j=0; j<n;j++){
            if (nums[j]==0){
                zeros ++;
            }
            
            while (zeros>1){
                if (nums[i]==0){
                    zeros--;
                }
                i++;                    
            }
            res = max(res, j - i);
        }
        return res;
    }
};