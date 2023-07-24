class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        bool wasSpace = false;

        for (int i=0; i < s.length(); ++i){
            if (s[i] != 32){ // not a space
                if (wasSpace){
                    length = 0;
                    wasSpace = false;
                }
                length += 1;
                
            } else {
                wasSpace = true;
            }
        }

        return length;
    }
};