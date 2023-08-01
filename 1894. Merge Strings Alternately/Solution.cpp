class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        int l3 = l1 + l2;
        int i = 0;
        int j = 0;
        string output = "";
        
        while (l3 > 0){
            if (l1-- > 0){
                output += word1[i++];
                --l3;
            }
            if (l2-- > 0){
                output += word2[j++];
                --l3;
            }
        }

        return output;

    }
};