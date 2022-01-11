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

def search_in_products(products, target_value):
    for idx in range(len(products)):
        if products[idx][0] == target_value:
            founded_product = products[idx]
            return founded_product
    raise ValueError("{} not in list".format(target_value))


def bfs(root_node, goal_value):

    # initialize frontier queue
    path_queue = deque()

    # add root path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    # search loop that continues as long as
    # there are paths in the frontier
    while path_queue:
        # get the next path and node
        # then output node value
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

        # check if the goal node is found
        if current_node.value == "Products:":
            print("Current node products: ", current_node.products)
            for product in current_node.products:
                if product[0] == goal_value:
                    current_path = product
                    return "Product found: " + str(current_path)

        # add paths to children to the  frontier
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    # return an empty path if goal not found
    return None


def dfs(root, target, path=()):
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        print(child)
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None


