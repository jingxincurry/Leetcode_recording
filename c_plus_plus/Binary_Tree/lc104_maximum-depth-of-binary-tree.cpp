/*
104.二叉树最大深度
输入：root = [3,9,20,null,null,15,7]
输出：3

2026.06.08
*/

#include<bits/stdc++.h>
#include<vector>
#include<iostream>

using namespace std;

struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr){}
};

vector<string> parseArray(string s){
    vector<string> res;
    string cur;
    for(char c: s){
        if(c == '[' || c == ']'){
            continue;
        }else if(c == ','){
            
        }

    }
}
TreeNode* buildTree(vector<string>& nodes){
    if(nodes.empty() || nodes)
}

