#include<iostream>
#include<stdio.h>
#include<vector>
#include <algorithm>
using namespace std;

vector<vector<int>> merge(vector<vector<int>> intervals)
{
    int n = intervals.size();
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end());
        int i = 0;
        while(i < n){
            int left = intervals[i][0];
            int right = intervals[i][1];
            while(i + 1 < n && right >= intervals[i+1][0])
            {
                
                right = max(right, intervals[i+1][1]);
                i++;
                
            }
            ans.push_back({left, right});
            i++;
        
        }
        return ans;
}

int main()
{
    vector<vector<int>> intervals1 = {{1,3}, {2,6}, {8, 10}, {15,18}};
    vector<vector<int>> ans = merge(intervals1);
    for (int i = 0; i < ans.size(); ++i) {
        cout << "[" << ans[i][0] << "," << ans[i][1] << "]";
    }
    std::cout << std::endl;
    return 0;
}