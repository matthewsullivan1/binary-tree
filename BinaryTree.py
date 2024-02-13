class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self) -> list:
        l = []
        self._preorder(self.root, l)

        return l
    def _preorder(self, node, l): #preorder helper
        if node:
            #print(str(node.value))
            l.append(node.value)
            self._preorder(node.left, l)
            self._preorder(node.right, l)

    def inorder_traversal(self) -> list:
        l = []
        self._inorder(self.root, l)
        return l
    def _inorder(self,node, l): #inorder helper
        if node:
            self._inorder(node.left, l)
            #print(str(node.value))
            l.append(node.value)
            self._inorder(node.right, l)

    def postorder_traversal(self) -> list:
        l = []
        self._postorder(self.root, l)
        return l
    def _postorder(self, node, l): #postorder helper
        if node:
            self._postorder(node.left, l)
            self._postorder(node.right, l)
            #print(str(node.value))
            l.append(node.value)

if __name__ == '__main__':

    # Create a binary tree
    bt = BinaryTree()
    bt.root = TreeNode(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)
    bt.root.right.left = TreeNode(6)
    bt.root.right.right = TreeNode(7)
    bt.root.left.left.left = TreeNode(8)
    bt.root.left.left.right = TreeNode(9)
    bt.root.right.right.right = TreeNode(10)

    # Test the traversals
    print("Preorder Traversal:", bt.preorder_traversal())
    print("Inorder Traversal:", bt.inorder_traversal())
    print("Postorder Traversal:", bt.postorder_traversal())

