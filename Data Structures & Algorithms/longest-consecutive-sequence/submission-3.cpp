class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        std::sort(nums.begin(), nums.end()); // sort with the default operator<, the order is ascending

        int current = nums[0], count=1, streak=1;

        for(int i=1; i<nums.size(); ++i)
        {
            if(nums[i] == current + 1)
                {
                    count ++;
                    if (count > streak)
                        streak = count;
                }
            else if (nums[i] > current)
            {
                count=1;
            }
            current = nums[i];
        }


        return streak;
    }
};
