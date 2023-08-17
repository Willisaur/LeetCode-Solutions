class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        vector<int> stack; // holds indices of zeros
        int streak = 0;
        int maxStreak = 0;

        for (int i=0; i<nums.size(); ++i){
            if (nums[i]){ // nums[i] == 1
                ++streak;
                if (streak > maxStreak){
                    maxStreak = streak;
                }
            } else { // nums[i] == 0
                if (stack.size() < k){
                    stack.push_back(i);
                    ++streak;
                    if (streak > maxStreak){
                        maxStreak = streak;
                    }
                } else if (k){
                    streak = i - stack[0];
                    stack.push_back(i);
                    stack.erase(stack.begin());
                } else if (streak){
                    if (k)
                        --streak;
                    else
                        streak = 0;
                }
            }
            cout << streak;
        }

        return maxStreak;
    }
};