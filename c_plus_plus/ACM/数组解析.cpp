/*
[1,1,2,0.0,5]


*/
#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

vector<string> parseArray(string s)
{
    vector<int> res;
    string cur;
    for(char c:s){
        if(c == '[' || c == ']' || c == ' '){
            continue;
        }else if(c == ','){
            if(!cur.empty()){
                res.push_back(stoi(cur));
                cur.clear();
            }
        }else{
            cur += c;
        }
    }
    if(!cur.empty()){
        res.push_back(stoi(cur));
    }
    return res;
}