class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def vertical_traverse(root, horizontal_distance, node_map):
    if root is None:
        return
    try:
        node_map[horizontal_distance].append(root.key)
    except KeyError:
        node_map[horizontal_distance] = [root.key]

    vertical_traverse(root.left, horizontal_distance - 1, node_map)
    vertical_traverse(root.right, horizontal_distance + 1, node_map)


def display_vertical_order(root):
    node_map = dict()
    horizontal_distance = 0
    vertical_traverse(root, horizontal_distance, node_map)

    result = []
    for value in sorted(node_map):
        result.extend(node_map[value])

    return result[::-1]


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    result = display_vertical_order(root)
    for element in result:
        print(element, end=" ")
