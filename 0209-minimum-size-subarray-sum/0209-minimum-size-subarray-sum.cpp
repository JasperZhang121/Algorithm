class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
        // using sliding window, move right pointer if the sum of subarray is smaller than target, move left pointer if the sum is larger than target, update the min length evey time deducing the left value
        
        int l=0,r=0, n=nums.size(),summ=0, res = INT_MAX;
        for(r = 0; r < n; r++) {
            summ += nums[r];
            while (summ >= target) {
                res = min(res, r - l + 1);
                summ -= nums[l];
                l++;
            }   
        }
        return res == INT_MAX ? 0 : res;
    }
};