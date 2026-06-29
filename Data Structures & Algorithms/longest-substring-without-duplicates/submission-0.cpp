class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 1. Use a set to store the seen characters
        // 2. If we see a duplicate we stop and slide the window
        // 3. We slide the starting point 
        // Complexity: time O(n) one pass, O(n) since we can potentially store the whole input
        unordered_set<char> charSet;
        int l = 0;
        int res = 0;

        for (int r = 0; r < s.size(); r++){
            while(charSet.find(s[r]) != charSet.end()){
                charSet.erase(s[l]);
                l++;
            }
            charSet.insert(s[r]);
            res = max(res, r-l+1);
        }
        return res;
    }
};
