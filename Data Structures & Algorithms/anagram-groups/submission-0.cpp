
class Solution
{
 public:
  vector<vector<string>> groupAnagrams(vector<string>& strs)
  {
    // 1. Since the input is constrained to english lowercase (ASCII),
    //    you can use a vector>int> to keep track the count of letters
    //    count[char - 'a']++;
    // 2. Convert the <char, count> pair as key for a hash_map, then push that
    // into result
    unordered_map<string, vector<string>> res;

    for (const auto& s : strs)
      {
        vector<int> count(26, 0);
        for (char c : s)
          {
            count[c - 'a']++;
          }
        string key = to_string(count[0]);
        for (int i = 1; i < 26; i++)
          {
            key += "," + to_string(count[i]);
          }
        res[key].push_back(s);  // res stores all strings that have same key
      }
    vector<vector<string>> result;
    for (const auto& pair : res)
      {
        result.push_back(pair.second);
      }
    return result;
  }
};
