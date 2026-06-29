class Solution {
 public:
  vector<int> twoSum(vector<int>& numbers, int target) {
    // This is a brute-force solution!!! Not a two pointer solution! Two pointer
    // solution is O(n)
    // With input = [-10, -8, -2, 1, 2, 5, 6], target = 0
    // the first sum is -4 which is smaller than the target (we need a bigger
    // value to get to result) move left pointer, i=1, j=6, sum = -2, move left
    // pointer again move left pointer, i=2, j=6, sum = 4, we have to move the
    // right pointer move right pointer, i=2, j=5, sum = 3, move right move
    // right pointer, i=2, j=4, sum = 0, solution found
    int i = 0, j = numbers.size() - 1;

    while (i != j) {
      // Solution found
      if (numbers[i] + numbers[j] == target) {
        return {i + 1, j + 1};
      }
      // move left pointer
      else if (numbers[i] + numbers[j] < target) {
        i++;
      }
      // move right pointer
      else {
        j--;
      }
    }
    return {};
  }
};