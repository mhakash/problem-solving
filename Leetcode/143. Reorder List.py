class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = None
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp 
        
        first, second = head, prev
        
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
        
        first.next = None
            
  