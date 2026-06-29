class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // We want K most frequent numbers!
        // 1. For each value >= count the number of occurences
        // 2. Order the map by its value, in decreasing order
        // 3. push k keys from the unordered_map
        std::unordered_map<int, int> counts; // values are initialized to zero?
        
        for(int num:nums)
        {
            counts[num]++;
        }
        
        std::vector<std::pair<int, int>> arr;
        for(const auto&p: counts)
        {
            arr.push_back({p.second, p.first}); // (count, number)
        }
        sort(arr.rbegin(), arr.rend());
        
        std::vector<int> result;
        for(int i=0; i<k; ++i){
            result.push_back(arr[i].second);
        }
        return result;
    }
};
