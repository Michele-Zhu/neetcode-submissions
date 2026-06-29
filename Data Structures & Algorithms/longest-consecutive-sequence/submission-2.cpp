class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        std::sort(nums.begin(), nums.end()); // sort with the default operator<, the order is ascending
        std::vector<int> consecutive_counts;
        int current = nums[0];
        int count = 1;
        consecutive_counts.push_back(1);
        for(int i=1; i<nums.size(); ++i)
        {
            if(nums[i] == current + 1)
                {count ++;
                consecutive_counts.push_back(count);}
            else if (nums[i] > current)
            {
                consecutive_counts.push_back(count);
                count=1;
            }
            current = nums[i];
        }

        sort(consecutive_counts.begin(), consecutive_counts.end(), [](int a, int b){
            return a>b;
        });
        return consecutive_counts[0];
    }
};
