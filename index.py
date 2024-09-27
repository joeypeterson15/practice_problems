
# 112. Path Sum
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node: return False
            currSum += node.val
            if currSum == targetSum: return True
            return dfs(node.left, currSum) or dfs(node.right, currSum)

        return dfs(root, 0)
    
    