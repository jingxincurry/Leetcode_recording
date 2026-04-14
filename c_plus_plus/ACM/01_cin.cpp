#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;

void test_cin()
{
    int num;
    cin >> num;
    cout << num << endl;
}

void test_different_num()
{
    vector<int> nums;
    int num;
    while (cin >> num)
    {
        nums.push_back(num);
        if(getchar() == '\n'){
            break;
        }
    }
    for(int i = 0; i < nums.size(); i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    

}


/*
2 3
1 2 3
1 2 3
*/
void two_array()
{
    int m;
    int n;
    cin >> m >> n;
    vector<vector<int>> matrix(m, vector<int>(n));
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cin >> matrix[i][j];
        }
    }

    //验证
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

/*
2 3
1,2,3
1,2,3
*/
void two_array_douhao()
{
    int m; // 接收行数
    int n; // 接收列数
    cin >> m >> n;
    cin.ignore();   // 吃掉上一行末尾的换行
    vector<vector<int>> matrix(m);
    for(int i = 0; i < m; i++){
        string s;
        getline(cin, s);
        // cin.ignore();  // 关键：忽略第一行末尾的换行符
        vector<int> vec;
        int p = 0;
        for(int q = 0; q < s.size(); q++){
            p = q;
            while(p < s.size() && s[p] != ','){
                p++;
            }
            string tmp = s.substr(q, p - q);
            vec.push_back(stoi(tmp));
            q = p;
        }
        //写入matrix
        matrix[i] = vec;
        vec.clear();
    }
    // 验证是否读入成功
    for(int i = 0; i < matrix.size(); i++) {
        for(int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    
}

int main()
{
    // test_cin();
    // test_different_num();
    // two_array();
    two_array_douhao();
    return 0;
}
