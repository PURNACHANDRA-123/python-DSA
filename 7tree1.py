#types of trees
#binary tree    #binary search tree
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def add_child(self,childnode):
        self.children.append(childnode)


    def __repr__(self):
        return str(self.data)
    #Pre-order Traversal (Root → Left → Right)
def dfs_preorder(node):
      if node is None:
        return
    
    # Visit the root node
      print(node.data, end=" ")
    
    # Visit each child (left to right)
      for child in node.children:
           dfs_preorder(child)



# Create the nodes
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")
node_f = TreeNode("F")

# Build the tree
root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)

# Example usage
dfs_preorder(root)  # Output: A B D E C F