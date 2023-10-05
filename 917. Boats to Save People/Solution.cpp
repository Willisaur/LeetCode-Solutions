class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int i = 0;
        int j = people.size();
        int count = 0;

        while (i <= --j){
            if (people[i] + people[j] <= limit){
                ++i;
            }
            ++count;
        }

        return count;
    }
};