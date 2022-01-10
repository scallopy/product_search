from collections import deque
from product_sort import quicksort


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.products = []

    def __repr__(self):
        stack = deque()
        stack.append([self, 0])
        level_str = "\n"
        while len(stack) > 0:
            node, level = stack.pop()

            if level > 0:
                level_str += "..." * (level-1) + "├─"
            if node.value:
                level_str += str(node.value)
                level_str += "\n"
                level += 1
                for child in reversed(node.children):
                    stack.append([child, level])
            if node.products:
                node.value = "Products:"
                level_str += "..." * (level-1) + "├─"
                level_str += str(node.value)
                level_str += "\n"
                level += 1
                for product in node.products:
                    level_str += "..." * (level-1) + "├─"
                    level_str += str(product)
                    level_str += "\n"
                level += 1
                # stack.append([, level])

        return level_str

    def add_child(self, child_node):
        # create parent child relationship
        # print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # remove parent child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traversal(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

    def add_product(self, name, description, price):
        self.products.append([name, description, price])
        # print("Adding product" +  str(self.products[-1]) + " to the " + str(self.value))
        quicksort(self.products, 0, (len(self.products)-1))
        # print("Sorted products: ", self.products)


def print_tree(root):
    stack = deque()
    stack.append([root, 0])
    level_str = "\n"
    level = 0
    while len(stack) > 0:
        node, level = stack.pop()

        if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
            level_str += "..." * (level-1) + "├─"
        elif level > 0:
            level_str += "..." + "└─"
        level_str += str(node.value)
        level_str += "\n"
        level += 1
        for child in node.children:
            stack.append([child, level])

    print(level_str)


def print_path(path):
    # If path is None, no path was found
    if path is None:
        print("No paths found!")

    # If a path was found, print path
    else:
        print("Path found:")
        for node in path:
            print(node.value)
