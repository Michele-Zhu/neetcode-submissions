
class Solution {
 public:
  vector<vector<int>> threeSum(vector<int>& nums) {
    // task: check if the sum of 3 values is equal to zero
    // problem: -4 + 0 +4 will result in zero
    // 1. Sort the vector
    // 2. Use three indexes to check the sums
    if (nums.size() < 3) return {};
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());  // O(n log(n)) complexity
    int left = 0, right = 0;

    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] > 0) break;
      if (i > 0 && nums[i] == nums[i - 1]) continue;

      left = i + 1, right = nums.size() - 1;
      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if (sum > 0) {
          right--;
        } else if (sum < 0) {
          left++;
        } else {
          result.push_back(vector<int>{nums[i], nums[left], nums[right]});
          left++, right--;
          while(left < right && nums[left] == nums[left-1])
          {
            left++;
          }
        }
      }
    }
    return result;
  }
};