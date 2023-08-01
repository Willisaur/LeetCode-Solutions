class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int max = 0;

        for (int n: candies){
            if (n > max){
                max = n;
            }
        }
        for (int n: candies){
            result.push_back(n + extraCandies >= max);
        }

        return result;
    }
};