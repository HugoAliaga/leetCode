class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p: return not q
        if not q: return not p
        #if p.val and not q.val: return False
        #if q.val and not p.val: return False
        if p.val != q.val: return False
        if p.left and not q.left: return False
        if q.left and not p.left: return False
        if not self.isSameTree(p.left,q.left): return False
        if p.right and not q.right: return False
        if q.right and not p.right: return False
        if not self.isSameTree(p.right,q.right): return False
        return True