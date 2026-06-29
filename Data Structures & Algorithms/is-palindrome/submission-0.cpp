class Solution
{
 public:
  bool isPalindrome(string s)
  {
    // The may be non alphanumerical characters inside the string!
    int left = 0, right = s.size() - 1;
    while (left < right)
      {
        // ignore non alphanumerical chars on the left
        while (left < right && !alphaNum(s[left]))
          {
            left++;
          }
        while (left < right && !alphaNum(s[right]))
          {
            right--;
          }
        if (tolower(s[left]) != tolower(s[right]))
          {
            return false;
          }
        left++;
        right--;
      }
    return true;
  }

  bool alphaNum(char c)
  {
    return ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') ||
            (c >= '0' && c <= '9'));
  }
};