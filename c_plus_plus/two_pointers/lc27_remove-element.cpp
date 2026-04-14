/*
27.移除元素

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。

date: 2026-04-09
*/
#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;

int removelement(vector<int>& nums, int val)
{
    int n = nums.size();
    int left = 0,right = 0;
    int k = 0;
    while(right < n){
        if(nums[right] != val){
            swap(nums[left], nums[right]);
            k++;
            left++;
        }
        right++;
    }
    return k;

}

int main()
{
    int n;
    cin >> n;
    int val;
    cin >> val;
    vector<int> nums(n);
    for(int i = 0; i < n;i++){
        cin >> nums[i];
    }
    int k = removelement(nums, val);
    for(int i = 0; i < k; i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}