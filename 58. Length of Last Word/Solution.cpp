class Solution {
public:
    int lengthOfLastWord(string s) {
        // iterate backwards since everything but the last word and surrounding whitespace is irrelevant
        // have a boolean which tracks whether a character has been counted yet
        // when the first character is counted, the bool switches states
        // the next whitespace causes a return of the length

        int length = 0;
        bool firstChar = false;
        int i = s.length();

        while (--i >= 0){
            if (s[i] != 32){
                firstChar = true;
                length += 1;
            } else if (firstChar){
                return length;
            }
        }

        return length;
    }
};