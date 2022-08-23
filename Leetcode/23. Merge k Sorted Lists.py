# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from queue import PriorityQueue

        dummy = ListNode()
        curr = dummy
        
        q = PriorityQueue(maxsize=len(lists))
        
        for index, node in enumerate(lists):
            if node: q.put((node.val, index, node))
                
        while q.qsize() > 0:
            poped = q.get()
            curr.next, index = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, index, curr.next))
        
        return dummy.next