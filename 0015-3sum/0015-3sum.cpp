class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(begin(nums),end(nums));
        vector<vector<int>> res;
        for (int i = 0; i < nums.size() && nums[i] <= 0; i++)
            if (i == 0 || nums[i - 1] != nums[i]) {
                twoSum(i,nums,res);
            }
        return res;
        
    }
    
    void twoSum(int i, vector<int>& nums, vector<vector<int>> &res){
        // assume the nums is sorted from low to high
        int l=i+1, r=nums.size()-1;
        while (l<r){
            int sum = nums[i]+nums[l]+nums[r];
            if (sum<0){
                // sum too small, increase the lower bar
                l++;
            }else if (sum>0){
                // sum too large, decrease the upper bar
                r--;
            }else{
                // exactly equal to 0, increase lower bar and decrease upper bar
                res.push_back({nums[i],nums[l++],nums[r--]});
                while (l<r && nums[l]==nums[l-1]){
                // no repeat tuple
                    l++;
                }
            }  
        }
    }
};