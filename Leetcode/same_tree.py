class Solution(object):
    def is_same_tree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_head = p
        q_head = q
        while p_head.left and p_head.right and q_head.left and p_head.right:
            if p_head.val == q_head.val:
                if p_head.left.val == q_head.left.val:
                    p_head = p_head.left
                    q_head = p_head.left
                elif p_head.left.val != q_head.left.val:
                    return False

                if p_head.right.val == q_head.right.val or p_head.right is None and q_head.right is None:
                    p_head = p_head.right
                    q_head = q_head.right
                elif p_head.right.val != q_head.right.val:
                    return False
            else:
                return False

        return True

