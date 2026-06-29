class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> hash_table;
        int res=0;

        for(int num:nums)
        {
            if(!hash_table[num])
            {
                hash_table[num] = hash_table[num-1] + hash_table[num+1] + 1;
                hash_table[num-hash_table[num-1]] = hash_table[num];
                hash_table[num + hash_table[num+1]] = hash_table[num];
                res = max(res, hash_table[num]);
            }
        }
        return res;
    }
};
