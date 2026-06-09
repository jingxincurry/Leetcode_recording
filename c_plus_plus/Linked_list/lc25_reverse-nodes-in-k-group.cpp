/*
25.K个元素翻转

2026.06.08
*/

#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;
struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(nullptr){}
};

ListNode* createList(const vector<int>& nums)
{
    if(nums.empty()) return nullptr;
    ListNode* head = new ListNode(nums[0]);
    ListNode* cur = head;
    for(int i = 1; i < nums.size(); i++){
        cur->next = new ListNode(nums[i]);
        cur = cur->next;
    }
    return head;
}

void printList(ListNode* head)
{
    ListNode* cur = head;
    while(cur){
        cout << cur->val;
        if(cur->next) cout << " ";
        cur = cur->next;
    }
    cout << endl;
}

ListNode* reverseKGroup(ListNode* head, int k)
{
    int n = 0;
    ListNode* cur = head;
    while(cur){
        n++;
        cur = cur->next;
    }
    ListNode dummy(0);
    dummy.next = head;
    ListNode* p0 = &dummy;
    ListNode* pre = nullptr;
    ListNode* cur = head;
    for(;n >=k; n -=k){
        for(int i = 0; i < k; i++){
            ListNode* nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        ListNode* nextemp = p0->next;
         
    }

}