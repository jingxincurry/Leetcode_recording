/*
274.H 指数

给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。

data:2026-05-09
*/
#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int hIndex(vector<int>& citations){
    sort(citations.begin(), citations.end());
        int n = citations.size();
        int left = 0, right = n - 1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(citations[mid] < n - mid){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return n - left;
}

int main()
{
    vector<int> citations = {3, 0, 6, 1, 5};
    int ans = hIndex(citations);
    cout << ans << " ";
}