#include<iostream>
#include<vector>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL) {}; 
};

ListNode* buildList(int n){
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        tail->next = new ListNode(x);
        tail = tail->next;
    }
    return dummy.next;
}
void printList(ListNode* head){
    while(head){
        cout << head->val;
        if(head->next) cout << " ";
        head = head->next;
    }
    cout << endl;
}

ListNode* reverseList(ListNode* head){
    ListNode* pre = NULL;
    ListNode* cur = head;
    while(cur){
        ListNode* nxt = head->next;
        head->next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}

int main()
{
    int n;
    cin >> n;

    ListNode* head = buildList(n);
    head = reverseList(head);

    printList(head);
    return 0;

}
