class Solution {
public:
    int climbStairs(int n) {
        // climbStairs(1) = 1
        // climbStairs(2) = 2
        vector<int> stairs{1, 2}; // initialize a vector with values 1 and 2/ terms 1 and 2

        for (int i = 3; i <=n; ++i){ // for all terms >= 3
            stairs.push_back(stairs[i-2] + stairs[i-3]); // add to the vector the sum of the last 2 values in the series
        }

        return stairs[n-1]; // return climbStairs(n) (n-1 because array is zero-indexed)
    }
};