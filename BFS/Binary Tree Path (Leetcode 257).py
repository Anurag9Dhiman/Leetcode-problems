class Solution:
    def binaryTreePath(self, root):
        res = []
        def dfs(node, path, result):

            if not root:
                return 
            path.append(str(node.val))

            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path, res)
                dfs(node.right, path, res)

            path.pop()
        dfs(root, [], res)
