/*
21.合并两个有序链表

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

ListNode* mergeTwoLists(ListNode* headA, ListNode* headB)
{
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    while(headA && headB){
        if(headA->val < headB->val){
            cur->next = headA;
            headA = headA->next;
        }else{
            cur->next = headB;
            headB = headB->next;
        }
        cur = cur->next;
    }
    if(headA){
        cur->next = headA;
    }else{
        cur->next = headB;
    }
    return dummy->next;
}

int main()
{
    // int m, n;
    // cin >> m >> n;
    // vector<int> nums1(m);
    // vector<int> nums2(n);
    // for(int i = 0; i < m; i++){
    //     cin >> nums1[i];
    // }
    // for(int i = 0; i < n; i++){
    //     cin >> nums2[i];
    // }
    // ListNode* headA = createList(nums1);
    // ListNode* headB = createList(nums2);
    // ListNode* dummy = mergeTwoLists(headA, headB);
    // printList(dummy);
    // return 0;
    vector<int> nums1{1, 2, 4};
    vector<int> nums2{1, 3, 4};
    ListNode* headA = createList(nums1);
    ListNode* headB = createList(nums2);
    ListNode* dummy = mergeTwoLists(headA, headB);
    printList(dummy);
    return 0;
}