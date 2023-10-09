# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = list()
        if len(head) % 2:
            middle = len(head) //2 +1
        else:
            middle = len(head) //2 +1
        new_list = head[:middle]
        return new_list 
    
