class Solution {
 public:
  int trap(vector<int>& height) {
    // water is trapped if the height[i] <= height[j], at this step you move the
    // pointers condition to move left pointer, right pointer edge conditions
    // 1. determine the amount of water m = 
    // peaks,
    //    we have min(height[i], height[j]) - height[i]
    // 2. conditions to move the pointers
    if (height.empty()) return 0;

    int trapped_water = 0;
    int i = 0, j = height.size() - 1;
    int leftMax = height[i], rightMax = height[j];
    while (i != j) {
      if (leftMax < rightMax) {
        i++;
        leftMax = max(leftMax, height[i]);
        trapped_water += leftMax - height[i];
      } else {
        j--;
        rightMax = max(rightMax, height[j]);
        trapped_water += rightMax - height[j];
      }
    }
    return trapped_water;
  }
};