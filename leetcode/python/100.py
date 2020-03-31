class Solution:
    def isSameTreeRec(self,p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or p:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTreeRec(p.left,q.left) and self.isSameTreeRec(p.right.q.left)

    from collections import deque

    def isSameTreeSeq(self, p, q):
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p,q),])
        while deq:
            p, q = deq.popleft()
            if not check(p,q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
