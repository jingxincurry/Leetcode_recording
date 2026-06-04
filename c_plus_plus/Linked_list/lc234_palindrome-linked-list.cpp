/*
234.回文链表

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
        if(cur->next) cout << " ";
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

bool isPalindrome(ListNode* head){
    if(head == nullptr || head->next == nullptr) return true;
    ListNode* slow = head;
    ListNode* fast = head;
    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    if(fast != nullptr){
        slow = slow->next;
    }
    ListNode* rever = reverseList(slow);
    ListNode* p1 = head;
    ListNode* p2 = rever;
    while(p1 && p2){
        if(p1->val != p2->val){
            return false;
        }
        p1 = p1->next;
        p2 = p2->next;
    }
    return true;
}

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    ListNode* head = createList(nums);
    if (isPalindrome(head)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    return 0;
}