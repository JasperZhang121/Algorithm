class Solution {
public:
    int rob(vector<int>& nums) {
        
        if (nums.size() == 1){
            return nums[0];
        }
        const int n = nums.size()+2;
        int dp1[n];
        dp1[n-1] = 0;
        dp1[n-2] = 0;
        for(int i=n-3; i>=1; i--){ //don't rob the first house
            dp1[i] = max(nums[i]+ dp1[i+2],dp1[i+1]);
        }
        //if we rob the first house, we couldn't rob the last one
        int dp2[n];
        dp2[n-1] = 0;
        dp2[n-2] = 0;
        dp2[n-3] = 0;//we set up the profit of last house as 0

        for(int i=n-4; i>=0; i--){ // rob the first house
            dp2[i] = max(nums[i]+ dp2[i+2],dp2[i+1]);
        }
        return max(dp1[1], dp2[0]);
    }
};