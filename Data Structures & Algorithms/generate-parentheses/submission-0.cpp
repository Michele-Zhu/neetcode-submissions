class Solution
{
  void backtrack(int openN, int closedN, int n, vector<string>& res,
                 string& stack)
  {
    // accept the solution
    if (openN == closedN && closedN == n)
      {
        res.push_back(stack);
        return;
      }

    if (openN < n)
      {
        stack += '(';
        backtrack(openN + 1, closedN, n, res, stack);
        stack.pop_back();  // remove the last character of the string
      }
    if (closedN < openN)
      {
        stack += ')';
        backtrack(openN, closedN + 1, n, res, stack);
        stack.pop_back();
      }
  }

 public:
  vector<string> generateParenthesis(int n)
  {
    // you can implement backtracking
    // 1. What is the reject condition of a string? The number of opening
    //    brackets is bigger than the number of close.
    // 2. When you accept the solution accept(P, n)? The number of open/close is
    //    equal and it is equal to the size of the problem
    vector<string> res;
    string stack;  
    backtrack(0, 0, n, res, stack);
    return res;
  }
};