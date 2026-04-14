/*
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

date: 2026-04-07

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
*/
#include<iostream>
#include<unordered_set>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

int longestConsecutive(vector<int>& nums){
    unordered_set<int> s(nums.begin(), nums.end());
    int longest = 0;

    for(int x: s){
        if(!s.count(x - 1)){  // s.find(x - 1) == s.end()
            int y = x + 1;
            int len = 1;
            while(s.count(y)){
                len++;
                y++;
            }
            longest = max(longest, len);
        }
    }
    return longest;
}

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    int ans = longestConsecutive(nums);
    cout << ans << endl;

}