/*
26.删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。

nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。

date:2026-04-14
*/
#include<vector>
#include<stdio.h>
#include<iostream>
using namespace std;


int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int k = 1;
        int left = 0,right = 1;
        while(right < n){
            if(nums[left] == nums[right])
            {
                right++;
            }else{
                nums[left+1] = nums[right];
                left++;
            }
        }
        return left + 1;
    }
int main()
{
    vector<int> nums1 = {1,1,1,2,2,3};
    int ans = removeDuplicates(nums1);
    cout << ans << endl;
    
}