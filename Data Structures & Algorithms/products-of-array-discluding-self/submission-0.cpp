class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Brute force: multiply for nested for loop. The result will be O(n^2)
        // Use a data structure to store prefix multiplication 
        vector<int> left = nums;
        vector<int> right = nums;
        int size = nums.size();

        for(int i=1; i<size; i++)
        {
            left[i] = left[i-1]*left[i];
        } 

        for(int i=right.size()-2; i>=0; i--)
        {
            right[i] = right[i+1] * right[i];
        }

        nums[0] = right[1];
        nums[size-1] = left[size-2];

        for(int i = 1; i<size-1; i++)
        {
            nums[i] = left[i-1] * right[i+1];
        }
        return nums;
    }
};
