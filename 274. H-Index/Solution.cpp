class Solution {
public:
    int hIndex(vector<int>& citations) {
        // sort the citations
        // store the lesser value: each element or the count of remaining elements
        // compare each value to a running max

        sort(citations.begin(), citations.end());
        vector<int> rem;
        int val;
        int max = 0;

        for (int i = 0; i < citations.size(); ++i){
            val = (citations[i] < citations.size()-i) ? citations[i] : citations.size()-i;
            if (val > max)
                max = val;
        }
        
        return max;
    }
};