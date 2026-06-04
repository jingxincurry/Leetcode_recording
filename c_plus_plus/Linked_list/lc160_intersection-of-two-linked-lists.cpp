/*
160. 相交链表
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

*/
#include<iostream>
#include<vector>
using namespace std;
struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL){};
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

// void freeList(ListNode* head){
//     while(head){
//         ListNode* temp = head;
//         head = head->next;
//         delete temp;
//     }
// }
ListNode* getIntersectionNode(ListNode *headA, ListNode *headB){
    ListNode* pA = headA;
    ListNode* pB = headB;
    while(pA!=pB){
        pA = pA ? pA->next:headB;
        pB = pB ? pB->next:headA;
    }
    return pA;
}

int main()
{
    int n,m;
    cin >> n >> m;
    vector<int> numsA(n);
    vector<int> numsB(m);
    
}