import dataclasses
from typing import Optional, Dict


input_path = 'input/7_No_Space_Left_On_Device.txt'


@dataclasses.dataclass
class TreeNode:
    name: str
    size: Optional[int] = 0
    parent: Optional['TreeNode'] = None
    children: Optional[Dict[str, 'TreeNode']] = None


@dataclasses.dataclass
class Tree:
    root: Optional[TreeNode] = TreeNode(name='/', parent=None, children={})
    total_size_of_small_dirs: Optional[int] = 0
    smallest_junk_size: Optional[int] = 0


def move_to_dir(current_node: TreeNode, command: str) -> TreeNode:
    directory = command.split('$ cd ')[1]
    if directory == '/':
        return current_node
    if directory == '..':
        return current_node.parent
    return current_node.children[directory]


def list_dir(current_node: TreeNode, command: str) -> TreeNode:
    return current_node


commands = {
    '$ cd ': move_to_dir,
    '$ ls': list_dir,
}


def build_tree():
    tree = Tree()
    current_node = tree.root
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            if line.startswith('$'):
                for k, v in commands.items():
                    if k in line:
                        current_node = v(current_node, line)
            else:
                if line.startswith('dir'):
                    name = line.split('dir ')[1]
                    if name not in current_node.children:
                        current_node.children[name] = TreeNode(name=name, parent=current_node, children={})
                else:
                    size, name = line.split()
                    if name not in current_node.children:
                        current_node.children[name] = TreeNode(
                            name=name, size=int(size), parent=current_node, children={}
                        )
    return tree


def dfs(node: TreeNode, tree: Tree):
    if node is None:
        return 0
    for child in node.children.values():
        size = dfs(child, tree)
        node.size += size
    if node.size <= 100000 and node.children:
        tree.total_size_of_small_dirs += node.size
    return node.size


def bfs(tree: Tree, need_to_free: int):
    a = [tree.root]
    tree.smallest_junk_size = tree.root.size
    while a:
        node = a.pop()
        if node is None:
            continue
        if node.size == need_to_free:
            tree.smallest_junk_size = node.size
            return
        elif node.size > need_to_free:
            if node.size < tree.smallest_junk_size:
                tree.smallest_junk_size = node.size
            for child in node.children.values():
                a.append(child)


def solution1(tree: Tree):
    return tree.total_size_of_small_dirs


def solution2(tree: Tree):
    need_to_free = 3 * 10**7 - (7 * 10**7 - tree.root.size)
    bfs(tree, need_to_free)
    return tree.smallest_junk_size


if __name__ == '__main__':
    tree = build_tree()
    dfs(tree.root, tree)
    print(solution1(tree))
    print(solution2(tree))
