class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // every input has exactly one pair of indices
        // This is a brute force solution
        for(int i = 0; i<nums.size(); i++)
        {
            for(int j = i + 1; j<nums.size(); j++)
            {
                if (nums[i]+nums[j] == target)
                    {
                        return {i, j};
                    }
            }
        }
        return {};
    }
};
