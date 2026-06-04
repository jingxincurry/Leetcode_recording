/*
189.轮转数组

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
date:2026.04.28
*/
#include<iostream>
#include<stdio.h>
#include<vector>
#include <algorithm>
using namespace std;

void rotatearray(vector<int>& nums, int k)
{
    int n = nums.size();
    k = k % n;
    reverse(nums.begin(),nums.end());
    reverse(nums.begin(),nums.begin()+k);
    reverse(nums.begin()+k,nums.end()); 
}

int main()
{
    int k;
    cin >> k;
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    rotatearray(nums, k);
    for(int i = 0; i < n; i++){
        cout << nums[i] << " ";
    }
}