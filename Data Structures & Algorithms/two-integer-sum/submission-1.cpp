class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // every input has exactly one pair of indices
        // Now I'm aiming for O(n) time & space solution
        // Hint: use HashMap
        unordered_map<int, int> indices; // (val, index)


        for(int i=0; i<nums.size(); i++)
        {
            // O(1)
            indices[nums[i]] = i; // O(1)
        }

        for(int i = 0; i<nums.size(); i++)
        {
            int diff = target - nums[i];
            if (indices.count(diff) && indices[diff] != i)
            {
                return {i, indices[diff]};
            }
        }
        /*
        for(int i = 0; i<nums.size(); i++)
        {
            for(int j = i + 1; j<nums.size(); j++)
            {
                if (nums[i]+nums[j] == target)
                    {
                        return {i, j};
                    }
            }
        }*/
        return {};
    }
};
