class Solution {
public:
    int search(vector<int>& nums, int target) {
        int i = 0; // start of the list
        int j = nums.size() -1; // end of the list
        int k = j / 2;

        while (i <= j){
            if (nums[k] == target){
                return k;
            }
            else if (nums[k] < target){
                i = k+1;
            } else {
                j = k-1;
            }
            k = (i + j) / 2;
        }
        return -1;
    }
};