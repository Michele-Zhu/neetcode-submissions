class Solution {
 public:
  vector<int> twoSum(vector<int>& numbers, int target) {
    size_t size = numbers.size();
    for (size_t i = 0; i < size; i++) {
      for (size_t j = i + 1; j < size; j++) {
        if (numbers[i] + numbers[j] == target) {
          return {i + 1, j + 1};
        }
      }
    }
    return {};
  }
};