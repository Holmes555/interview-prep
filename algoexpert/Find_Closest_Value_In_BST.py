def findClosestValueInBst(tree, target):
    def find_target(node, closest):
        if node is None:
            return closest[0]
        diff = abs(target - node.value)
        if diff < closest[1]:
            closest = (node.value, diff)
        if target > node.value:
            return find_target(node.right, closest)
        else:
            return find_target(node.left, closest)

    return find_target(tree, (tree.value, abs(tree.value - target)))


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
