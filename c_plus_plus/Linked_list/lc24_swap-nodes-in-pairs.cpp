/*
24.两两交换链表中的节点
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

2026.06.04
*/
#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x): val(x),next(nullptr){}
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
ListNode* swapPairs(ListNode* head)
{
    ListNode dummy(0);
    dummy.next = head;
    ListNode* node0 = &dummy;
    ListNode* node1 = head;
    while(node1 && node1->next){
        ListNode* node2 = node1->next;
        ListNode* node3 = node2->next;

        node0->next = node2;
        node2->next = node1;
        node1->next = node3;

        node0 = node1;
        node1 = node3;
    }
    return dummy.next;
}

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    ListNode* head = createList(nums);
    ListNode* dummy = swapPairs(head);
    printList(dummy);
    return 0;
}