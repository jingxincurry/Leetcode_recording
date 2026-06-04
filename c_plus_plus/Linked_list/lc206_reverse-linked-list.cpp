/*
206.反转链表
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

ListNode* reverseList(ListNode* head){
    ListNode* pre = nullptr;
    ListNode* cur = head;
    while(cur){
        ListNode* nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    ListNode* head = createList(nums);
    head = reverseList(head);
    printList(head);
    return 0;

}