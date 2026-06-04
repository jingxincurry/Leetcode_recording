#include<queue>
#include<iostream>
#include<stdio.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k)
{
    int n = nums.size();
    deque<int> dp;
    vector<int> ans;
    for(int i = 0; i < n; i++)
    {
        while(!dp.empty() && nums[dp.back()] <= nums[i]){
            dp.pop_back();
        }
        dp.push_back(i);
        if(i - k >= dp.front()){
            dp.pop_front();
        }
        if(i >= k - 1){
            ans.push_back(nums[dp.front()]);
        }
    }
    return ans;
}
int main()
{
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    
    int k = 3;
    vector<int> ans = maxSlidingWindow(nums, k);
    int n = ans.size();
    for(int i = 0; i < n; i++)
    {
        cout << ans[i] << " ";
    }
    return 0;
}