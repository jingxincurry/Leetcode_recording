/*
92.反转链表2
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

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
    ListNode(int x): val(x),next(nullptr){}
};

ListNode* createList(const vector<int>& nums){
    if(nums.empty()) return nullptr;
    ListNode* head = new ListNode(nums[0]);
    ListNode* cur = head;
    for(int i = 1; i < nums.size(); i++){
        cur->next = new ListNode(nums[i]);
        cur = cur->next;
    }
    return head;
}

void printList(ListNode* head){
    ListNode* cur = head;
    while(cur){
        cout << cur->val;
        if(cur->next!=nullptr) cout << " ";
        cur = cur->next;
    }
    cout << endl;
}

ListNode* reverseBetween(ListNode* head, int left, int right)
{
    ListNode dummy(0);
    dummy.next = head;
    ListNode* p0 = &dummy;
    
    for(int i = 0; i < left - 1; i++){
        p0 = p0->next;
    }
    ListNode* cur = p0->next;
    ListNode* pre = nullptr;
    int len = right - left + 1;
    while(len > 0){
        ListNode* nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
        len--;
    }
    p0->next->next = cur;
    p0->next = pre;
    return dummy.next;
}

int main()
{
    int n,left,right;
    cin >> n;
    cin >> left >> right;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    ListNode* head = createList(nums);
    ListNode* dummy = reverseBetween(head, left, right);
    printList(dummy);
    return 0;
}