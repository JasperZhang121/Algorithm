class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        unordered_set<long> set;
        long sumNum = 0;
        
        // convert vector to set
        for (int num : nums){
            set.insert((long)num);
            sumNum += num;
        }
        
        // calculate sum
        long sumSet = 0;
        for (int num:set){
            sumSet += num;
        }
        
        // res = (sumSet*3-sumNum)/2
        return (int)((sumSet*3-sumNum)/2);
    }
};