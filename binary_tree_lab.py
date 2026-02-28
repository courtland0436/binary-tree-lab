from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Computes the maximum depth of a binary tree using recursion.
    """
    # Base Case: If the node is None, depth is 0
    if not root:
        return 0
    
    # Recursive step:
    # 1. Get the depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # 2. Return the maximum of the two + 1 (for the current node)
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the LCA of two nodes in a Binary Search Tree (BST).
    """
    # Design Consideration: Utilize BST properties to navigate the tree.
    
    # If both p and q are less than the root, LCA is in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both p and q are greater than the root, LCA is in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # Otherwise, this root is the split point, so it is the LCA
    return root