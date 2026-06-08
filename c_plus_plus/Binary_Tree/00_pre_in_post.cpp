/*
前中后序遍历

*/
#include<iostream>
#include<stdio.h>
#include<vector>
#include<bits/stdc++.h>
using namespace std;
struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x),left(nullptr),right(nullptr){}
};

TreeNode* buildTree(const vector<int>& nums)
{
    if(nums.empty() || nums[0] == 0){
        return nullptr;
    }

    TreeNode* root = new TreeNode(nums[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while(!q.empty() && i < nums.size()){
        TreeNode* cur = q.front();
        q.pop();
        if(i < nums.size() && nums[i] != 0){
            cur->left = new TreeNode(nums[i]);
            q.push(cur->left);
        }
        i++;
        if(i < nums.size() && nums[i] != 0){
            cur->right = new TreeNode(nums[i]);
            q.push(cur->right);
        }
        i++;
    }
    return root;
}

//前序
void preorder(TreeNode* root,vector<int>& res)
{
    if(!root) return;
    res.push_back(root->val);
    preorder(root->left, res);
    preorder(root->right, res);
}

vector<int> preorderTraversal(TreeNode* root){
    vector<int> res;
    preorder(root, res);
    return res;
}


//中序
void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    cout << root->val << " ";
}

void printVector(const vector<int>& nums)
{
    for(int i = 0; i < nums.size(); i++){
        if(i > 0) cout << " ";
        cout << nums[i];
    }
    cout << endl;
}

int main()
{
    //输入格式：树的层序遍历，0表示空节点
    //例如：1 2 3 0 0 4 5表示如下树：
    //     1
    //    / \
    //   2   3
    //      / \
    //     4   5
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    TreeNode* root = buildTree(nums);
    vector<int> pre = preorderTraversal(root);
    printVector(pre);
    return 0;
}