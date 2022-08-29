# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            currLevel = []
            
            for i in range(qLen):
                item = q.popleft()
                currLevel.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            
            res.append(currLevel)
        
        return res