class Solution {
public:
    int climbStairs(int n) {
        vector<int> stairs{1, 2};

        for (int i = 3; i <=n; ++i){
            stairs.push_back(stairs[i-2] + stairs[i-3]);
        }

        return stairs[n-1];
    }
};