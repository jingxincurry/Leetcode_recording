/*
438.找到字数串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

date:2026-04-14
*/

#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        vector<int> s_cnt(26,0),p_cnt(26,0);
        int m = s.length(), n = p.length();
        for(char c:p){
            p_cnt[c-'a']++;
        }
        int left = 0,right = 0;
        while(right < m){
            s_cnt[s[right]-'a']++;
            
            if(right - left + 1 > n){
                s_cnt[s[left]-'a']--;
                left++;
            }
            if(s_cnt == p_cnt){
                ans.push_back(left);
            }
            right++;
        }
        return ans;
    }

int main()
{
    string s1 = "cbaebabacd";
    string p1 = "abc";

    vector<int> ans;
    ans = findAnagrams(s1, p1);
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << " ";
    }
}