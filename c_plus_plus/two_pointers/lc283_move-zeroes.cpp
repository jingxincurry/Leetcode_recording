/*
283.移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

date: 2026-04-09
*/
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

void moveZeroes(vector<int>& nums){
    int n = nums.size();
    int left = 0, right = 0;
    while(right < n){
        if(nums[right] != 0){
            swap(nums[right], nums[left]);
            left++;
        }
        right++;
    }
}

int main()
{
    // int n;
    // cin >> n;
    // vector<int> nums(n);
    // for(int i = 0; i < n; i++){
    //     cin >> nums[i];
    // }
    // moveZeroes(nums);
    // for(int i = 0; i < n; i++){
    //     cout << nums[i] << ' ';
    // }
    // return 0;


    vector<int> nums1 = {0, 1, 0, 3, 12};
    moveZeroes(nums1);
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i] << ' ';

    }
    cout << '\n';
    return 0;
}