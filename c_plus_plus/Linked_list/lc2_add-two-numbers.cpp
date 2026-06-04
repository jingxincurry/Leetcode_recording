/*
2.两数想加

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

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
{
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    int carry = 0;
    while(l1 || l2 || carry){
        if(l1){
            carry += l1->val;
            l1 = l1->next;
        }
        if(l2){
            carry += l2->val;
            l2 = l2->next;
        }
        cur->next = new ListNode(carry % 10);
        cur = cur->next;
        carry /= 10;
    }
    return dummy->next;
}

int main()
{
    int m, n;
    cin >> m >> n;
    vector<int> nums1(m);
    vector<int> nums2(n);
    for(int i = 0; i < m; i++){
        cin >> nums1[i];
    }
    for(int i = 0; i < n; i++){
        cin >> nums2[i];
    }
    ListNode* l1 = createList(nums1);
    ListNode* l2 = createList(nums2);
    ListNode* dummy = addTwoNumbers(l1, l2);
    printList(dummy);
    return 0;
}