
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 1);
        int pre = 1;
        for(int i = 1; i < n; i++){
            pre = pre * nums[i - 1];
            ans[i] *= pre;
        }
        int suf = 1;
        for(int i = n - 2; i >= 0; i--){
            suf *= nums[i + 1];
            ans[i] *= suf;
        }
        return ans;
    }

int main()
{
    vector<int> nums = {1, 2, 3, 4};
    vector<int> ans = productExceptSelf(nums);
    for(int i = 0; i < nums.size(); i++){
        cout << ans[i] << " ";
    }
}