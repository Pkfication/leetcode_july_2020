# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        h = self.height(root)
        r = []
        for i in reversed(range(1, h+1)):
            lvl = []
            self.printGivenLevel(root,i, lvl)
            r.append(lvl)
        return r

    def printGivenLevel(self, root, level, arr): 
        if root is None: 
            return 
        if level ==1 : 
            arr.append(root.val)

        elif level>1: 
            self.printGivenLevel(root.left, level-1, arr) 
            self.printGivenLevel(root.right, level-1, arr) 
 
    def height(self, node): 
        if node is None: 
            return 0 
        else: 
            lheight = self.height(node.left) 
            rheight = self.height(node.right) 

            if lheight > rheight : 
                return lheight + 1
            else: 
                return rheight + 1
