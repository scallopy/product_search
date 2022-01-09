from model_tree import TreeNode


root_node = TreeNode("Stores")

hardware_store = TreeNode("Hardware Store")
souvenirs_store = TreeNode("Souvenirs")
services = TreeNode("Services")

root_node.add_child(hardware_store)
root_node.add_child(souvenirs_store)
root_node.add_child(services)

hardware_store.add_child(TreeNode("Bath"))
hardware_store.add_child(TreeNode("Building Materials"))
hardware_store.add_child(TreeNode("Cleaning"))
hardware_store.add_child(TreeNode("Lighting"))

print(root_node)
"""
for child in root_node.children:
    print()
    print("Store: ", child)
    for item in child.children:
        print()
        print("Category: ", item)
"""
