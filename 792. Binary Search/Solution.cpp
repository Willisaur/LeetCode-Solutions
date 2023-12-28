class Solution {
public:
    int search(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size()-1;
        int k = nums.size() / 2;

        while (i <= j){
            if (nums[k] == target){
                return k;
            }
            if (nums[k] < target)
                i = k+1;
            else 
                j = k-1;
            k = (i+j)/2;
        }

        return -1;
    }
};