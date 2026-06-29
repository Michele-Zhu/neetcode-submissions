class Solution {
public:
    int characterReplacement(string s, int k) {
        // Naive solution
        // int result=0;
        unordered_map<char, int> count;
        int result = 0;
        int l=0, max_frequency;
        for (int r = 0; r<s.size(); r++)
        {
            count[s[r]]++;
            max_frequency = max(max_frequency, count[s[r]]);

            // Exit condition, i.e. move to next window start
            while((r-l+1) - max_frequency > k){
                count[s[l]]--;
                l++;
            }
            result = max(result, r-l+1);
        }
        return result;
    }
};
