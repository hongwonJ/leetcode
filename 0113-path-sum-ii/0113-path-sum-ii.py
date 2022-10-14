class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        path_list = []

        def dfs(root, path):

            if root != None:
                path.append(root.val)

                # if node is leaf
                if root.left == None and root.right == None and sum(path) == targetSum:
                    path_list.append(path[:])

                # moving to the left        ## update the list 
                if root.left:
                    dfs(root.left, path)
                    path.pop()

                # moving to the right
                if root.right:
                    dfs(root.right, path)
                    path.pop()
    
        dfs(root, [])
        
        return path_list 
        