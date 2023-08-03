class Solution {
public:

    bool isVowel(char& c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }

    string reverseVowels(string s) {
        if (s.length() == 1){
            return s;
        }

        vector<char> read_vowels;
        int i=0;
        string output = "";

        for (char c: s){
            if (isVowel(c)){
                read_vowels.push_back(c);
                ++i;
            }
        }

        --i;

        for (int j = 0; j < s.length(); ++j){
            if (isVowel(s[j])){
                output += read_vowels[i--];
            } else{
                output += s[j];
            }
        }

        return output;
    }
};