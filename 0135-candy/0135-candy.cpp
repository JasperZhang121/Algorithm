class Solution {
public:
    int candy(vector<int>& ratings) {
        
        int size = ratings.size();
        if (size<2) return size;
        vector<int> num(size,1); // initialize to array with ones
        
        for (int i=1;i<size;i++){
             if (ratings[i]>ratings[i-1]){
                 num[i] = num[i-1]+1;
             }   
        }
        
        for (int i= size-1;i>0;i--){
            if (ratings[i]<ratings[i-1]){
                num[i-1] = max(num[i-1],num[i]+1);
            }            
        }
        return accumulate(num.begin(),num.end(),0) ;
    }
};