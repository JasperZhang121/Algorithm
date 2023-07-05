class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        // same number appear twice will be cancelled by X0R
        // example: 2^2 = 
        //              ->    10
        //              ->    10
        //              =     00
        
        int res = 0;
        for (auto x: nums){
            res ^= x;
        }
        return res; 
    }
};