class Solution {
public:
    string mult(string s, int t){
        string temp = "";
        while (t-- > 0){
            temp += s;
        }
        return temp;
    }
    string gcdOfStrings(string str1, string str2) {
        // str 1 will always be the longer string
        if (str1.length() < str2.length()){
            string temp = str1;
            str1 = str2;
            str2 = temp;
        }

        int i = str2.length();
        int s1l = str1.length();
        int s2l = str2.length();

        while (i > 0){
            if (s1l % i == 0 && s2l % i == 0){
                string sub = str2.substr(0, i);
                string dup1 = mult(sub, s1l/i);
                string dup2 = mult(sub, s2l/i);
                cout << i << sub << dup1 << dup2;
                if (str1 == dup1 && str2 == dup2){
                    return sub;
                }
            }
            --i;
        }
        return "";
    }
};