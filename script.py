from model_tree import TreeNode, bfs


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

print(root_node)


print()
goal_value, goal_path = bfs(root_node, "Some")
print(goal_value)

if goal_path is None:
    print("No path found")
else:
    print("Path found")
    path = ""
    for node in goal_path:
        path += node.value + " => "
    print(path + goal_value)


# new_path = dfs(root_node, "Cleaning")
# print("Dfs path: ", new_path)
