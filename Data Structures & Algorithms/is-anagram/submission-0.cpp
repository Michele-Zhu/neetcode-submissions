class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int m = t.size();
        if (n!=m)
            return false;
        unordered_map<char, int> hash_table_s;
        unordered_map<char, int> hash_table_t;
        for(char c:s)
            {
                hash_table_s[c]++;
            }

        for(char c:t)
            {
                hash_table_t[c]++;
            }
        for(auto[key, val]: hash_table_s)
        {
            if(hash_table_t[key] != val)
                return false;
        }
        return true;
    }
};
