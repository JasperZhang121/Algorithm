class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        string result = "";
        int i = 0;
        while (i < word1.length() && i < word2.length()) {
            result += word1[i];
            result += word2[i];
            i++;
        }
        result += word1.substr(i) + word2.substr(i);
        return result;
        
    }
};