from collections import deque
from random import randrange


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
                for product in node.products:
                    level_str += "..." * (level-1) + "├─"
                    level_str += str(product)
                    level_str += "\n"
                level += 1

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

    def remove_product(self, product_name):
        path_queue = deque()
        initial_path = [self]
        path_queue.appendleft(initial_path)
        while path_queue:
            current_path = path_queue.pop()
            current_node = current_path[-1]

            # check if the goal node is found
            if current_node.products:
                for product in current_node.products:
                    if product[0] == product_name:
                        print("Current node products: ", current_node.products)
                        current_node.products.remove(product)
                        print("Current node products: ", current_node.products)
                        return "Removed product: " + str(product)

            for child in current_node.children:
                new_path = current_path[:]
                new_path.append(child)
                path_queue.appendleft(new_path)

        # return an empty path if goal not found
        return None




def product_bfs(root_node, goal_value):

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
        if current_node.products:
            print("Current node products: ", current_node.products)
            for product in current_node.products:
                if product[0] == goal_value:
                    return current_path, ("Product found: " + str(product))

        # add paths to children to the  frontier
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    # return an empty path if goal not found
    return None


def quicksort(arr, start, end):
    count = 0
    if start >= end:
        return arr
    pivot_idx = randrange(start, end)
    pivot_element = arr[pivot_idx]

    count += 1
    # print("Pivot element: ", pivot_element)
    # print("Iterations: ", count)
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    less_than_pointer = start
    for idx in range(start, end):
        if arr[idx][0][0] < pivot_element[0][0]:
            arr[idx], arr[less_than_pointer] = arr[less_than_pointer], arr[idx]
            less_than_pointer += 1

    arr[less_than_pointer], arr[end] = arr[end], arr[less_than_pointer]
    quicksort(arr, start, less_than_pointer - 1)
    quicksort(arr, less_than_pointer + 1, end)

    start += 1
    return quicksort(arr, start, end)


