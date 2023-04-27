# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.left)) + 1


def main():
    # root = [3, 9, 20, null, null, 15, 7]
    three = TreeNode(val=3)
    nine = TreeNode(val=9)
    twenty = TreeNode(val=20)
    fifteen = TreeNode(val=15)
    seven = TreeNode(val=7)
    three.left = nine
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seven
    s = Solution()
    print(s.minDepth(three))


if __name__ == '__main__':
    main()
