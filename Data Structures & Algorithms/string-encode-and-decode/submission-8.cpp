class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()) return "";
        string res;
        for(const string& s: strs)
        {
            res += to_string(s.size()) + "#" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i=0;
        while(i<s.size())
        {   
            int j; // index used to parse the word 
            j = i;
            while(s[j] != '#')
            {
                j++;  // j points at position of #
            }
            int length = stoi(s.substr(i, j - i));
            i = j+1;  // move i after the #
            j = i + length;  // position after the word, i.e. new number if exist
            res.push_back(s.substr(i, length));
            i = j; // position the pointer after the word
        }
        return res;
    }
};
