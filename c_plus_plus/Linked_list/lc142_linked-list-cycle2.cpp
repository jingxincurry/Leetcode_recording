/*
142. 环形链表2
*/
#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

struct ListNode{
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

void createCycle(ListNode* head, int pos){
    if(head == nullptr || pos == -1) return;
    ListNode* cur = head;
    ListNode* cycleNode = nullptr;
    int index = 0;
    while(cur->next){
        if(index == pos){
            cycleNode = cur;
        }
        cur = cur->next;
        index++;
    }
    if (index == pos) {
        cycleNode = cur;
    }
    if(cycleNode!=nullptr){
        cur->next = cycleNode;
    }
}

ListNode* hasCycle2(ListNode* head)
{
    ListNode* slow = head;
    ListNode* fast = head;
    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            while(slow!=head){
                slow = slow->next;
                head = head->next;
            }
            return slow;
        }
    }
    return nullptr;
}

int main()
{
    int n, pos;
    cin >> n >> pos;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    ListNode* head = createList(nums);
    createCycle(head, pos);
    ListNode* ans = hasCycle2(head);
    if (ans == nullptr) {
        cout << "null" << endl;
    } else {
        cout << ans->val << endl;
    }
    
}