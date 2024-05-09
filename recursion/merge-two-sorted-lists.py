# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #list1 is head of list1
        #list2 is the head of list2

        result = ListNode()
        root = result

        while list1 and list2:
            if list2.val < list1.val:
                root.next = list2
                list2 = list2.next
            else:
                root.next = list1
                list1 = list1.next
            
            root = root.next
        
        if list1:
            root.next = list1
        elif list2:
            root.next = list2

        return result.next

        
        