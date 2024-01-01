/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1==null && list2==null){
            return list1;
        }
        ListNode head = list1;

        // put first node in head
        if (list1==null || list2!=null && list1.val>list2.val){
            head = list2;
            list2 = list2.next;
        } else {
            list1 = list1.next;
        }
        ListNode tail = head;

        // add next least element to the tail while each list has an element
        while (list1 != null && list2 != null){
            if (list1.val <= list2.val){
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        // remaining elements go at the end
        tail.next = (list1!=null) ? list1 : list2;

        return head;
    }
}