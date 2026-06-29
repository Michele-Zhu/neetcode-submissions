class Solution {
 public:
  int maxArea(vector<int>& height) {
    // area calculation is (j-i)*min(height[i], height[j])
    int i = 0, j = height.size() - 1;
    int maxArea = 0;
    int area = 0;
    while (i != j) {
      area = (j - i) * min(height[i], height[j]);
      if (area > maxArea) {
        maxArea = area;
      }

      if (height[i] > height[j]) {
        j--;
      } else {
        i++;
      }
    }
    return maxArea;
  }
};