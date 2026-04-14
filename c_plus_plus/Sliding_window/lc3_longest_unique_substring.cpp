/*
3.无重复字符最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

date:2026-04-09
*/
#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

int lengthOfLongestSubstring(string s)
{
    int n = s.length();
    unordered_map<int> mp;
    int left = 0,right = 0;
    while(left < right){
        ms[s[right]]++;
    }
    return 0;
}
int main()
{
    string s = "abcabcbb";
    cout << lengthOfLongestSubstring(s) << endl;
    
    return 0;
    
}