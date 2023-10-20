class Solution {
public:
    int fib(int n) {
        // fib(0) = 0
        // fib(1) = 1
        // fib(2) = 1
        vector<int> dp{0, 1}; // initialize vector with values 0 and 1/ terms 0 and 1

        for (int i = 2; i <=n ; ++i){ // any terms for n >= 2
            dp.push_back(dp[i-1] + dp[i-2]); // add to the vector the sum of the last 2 fib values
        }

        return dp[n]; // return fib(n)
    }
};