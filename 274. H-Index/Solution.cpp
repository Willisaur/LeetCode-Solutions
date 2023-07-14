class Solution {
public:
    int hIndex(vector<int>& citations) {
        // sort the citations
        // compare each element to the count of remaining elements; store the lesser value
        // return the max of that list

        sort(citations.begin(), citations.end());
        vector<int> rem;
        int val;

        for (int i = 0; i < citations.size(); ++i){
            val = (citations[i] < citations.size()-i) ? citations[i] : citations.size()-i;
            rem.push_back(val);
        }
        
        val = 0;

        for (int n: rem){
            if (n > val)
                val = n;
        }

        return val;
    }
};