class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
       vector<int> result(temperatures.size(), 0);
       stack<pair<int, int>> stack; // pair: {temp, idx}

       for (int i = 0; i<temperatures.size(); i++)
       {
        int t = temperatures[i];
        while(!stack.empty() && t > stack.top().first)
        {
            auto pair = stack.top();
            stack.pop();
            result[pair.second] = i - pair.second;
        }
        stack.push({t, i});
       }
       return result;
    }
};
