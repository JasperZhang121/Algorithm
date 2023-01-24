class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int child = 0 , cookies = 0;
        while ( child<g.size() && cookies < s.size() ){
            if (g[child]<=s[cookies]) ++child;
            ++cookies;
        }
        return child;
    }
};