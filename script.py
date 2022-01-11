from model_tree import TreeNode, product_bfs

# Build Tree
root_node = TreeNode("Stores")

hardware_store = TreeNode("Hardware Store")
souvenirs_store = TreeNode("Souvenirs")
services = TreeNode("Services")

root_node.add_child(hardware_store)
root_node.add_child(souvenirs_store)
souvenirs_store.add_product("Clock", "Old Clock", 56)
root_node.add_child(services)

bath = TreeNode("Bath")
hardware_store.add_child(bath)
tools = TreeNode("Tools")
hardware_store.add_child(tools)

hand_tools = TreeNode("Hand Tools")
tools.add_child(hand_tools)
hand_tools.add_product("Some", "Something", 121)
hand_tools.add_product("This", "Thisthing", 12)
hand_tools.add_product('Mine', 'Description', 23)
hand_tools.add_product('Asterisks', 'Description', 1222)
hand_tools.add_product('Nolan', 'Description', 34)

electrical_tools = TreeNode("Electrical Tools")
tools.add_child(electrical_tools)

building_materials = TreeNode("Building Materials")
hardware_store.add_child(building_materials)
cleaning = TreeNode("Cleaning")
hardware_store.add_child(cleaning)
lighting = TreeNode("Lighting")
hardware_store.add_child(lighting)
lighting.add_product("Lamp", "lighting", 24)


print("Many stores and the products in them represented with Tree Node:")
print(root_node)


print()
print("Searching for a product in stores: ")
print()
goal_path, goal_value = product_bfs(root_node, "Some")
print()
if goal_path is None:
    print("No path found")
else:
    print("Product and Path found:")
    path = ""
    for node in goal_path:
        path += node.value + " => "
    print(path + goal_value)

print()
print("Remove product:")
print(root_node.remove_product("Some"))
