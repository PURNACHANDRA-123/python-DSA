class BinarytreesNode:
    def __init__(self,data):             #In-order Traversal (Left → Root → Right)
        self.data=data
        self.left=None
        self.right=None

    def inorder_dfs(self,node):
        if node is None:
            return
        
        self.inorder_dfs(node.left)
        print(node.data,end=" ")
        self.inorder_dfs(node.right)
    def outorders_dfs(self,node):  #Post-order Traversal (Left → Right → Root)
        if node is None:
            return
        self.outorders_dfs(node.left)
        self.outorders_dfs(node.right)
        print(node.data,end=" ")

root=BinarytreesNode(1)
root.left=BinarytreesNode(2)
root.right=BinarytreesNode(3)
root.left.left = BinarytreesNode(4)
root.left.right = BinarytreesNode(5)

print("In-order traversal:")
root.inorder_dfs(root) 
print("\nPre-order traversal:")
root.outorders_dfs(root)


