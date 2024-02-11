# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def solution(self, root):
        
        if root is None:
            return 0, 0
        
        left_path, max_path_left = self.solution(root.left) 
        right_path, max_path_right = self.solution(root.right)
        
        max_path = max(left_path + right_path , max_path_right)
        max_path = max(max_path , max_path_left)
        return max(left_path , right_path) + 1 , max_path
        
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # print(self.solution(root.left))
        # print(self.solution(root.right))
        left_path, max_path_left = self.solution(root.left) 
        right_path, max_path_right = self.solution(root.right)
        max_path = max(left_path + right_path , max_path_right)
        max_path = max(max_path , max_path_left)
        
        
        return max(left_path + right_path , max_path)