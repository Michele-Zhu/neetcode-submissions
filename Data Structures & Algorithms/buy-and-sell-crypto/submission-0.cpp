class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // How many times I can buy and sell? Unlimited?
        // No you can only buy one day and sell in a different day
        // use two trackers left and right
        int l=0, r=1, max_profit=0;
        // profit = max(profit, prices[l]-prices[r])
        while(r < prices.size())
        {
            // There is a day where price is higher
            if (prices[l] < prices[r])
            {
                max_profit = max(max_profit, prices[r] - prices [l]);
            }
            else // There is a day where price is lower
            {
                l = r;
            }
            r++;
        }
        return max_profit;
    }
};
