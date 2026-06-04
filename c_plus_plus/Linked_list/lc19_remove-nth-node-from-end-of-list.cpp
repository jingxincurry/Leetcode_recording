/*
19.删除链表倒数第n个节点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

删除节点要建一个虚拟节点

2026.06.04
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

ListNode* removeNthFromEnd(ListNode* head, int n)
{
    ListNode dummy(0);
    dummy.next = head; 
    ListNode* slow = &dummy;
    ListNode* fast =&dummy;
    for(int i = 0; i < n; i++){
        fast = fast->next;
    }
    while(fast->next){
        slow = slow->next;
        fast = fast->next;
    }
    slow->next = slow->next->next;
    return dummy.next;
}

int main()
{
    int m;
    cin >> m;
    int n;
    cin >> n;
    vector<int> nums(m);
    for(int i = 0; i < m; i++){
        cin >> nums[i];
    }
    ListNode* dummy = createList(nums);
    dummy = removeNthFromEnd(dummy, n);
    printList(dummy);
    return 0;

}