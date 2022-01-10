from model_tree import TreeNode


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

"""
print()
for child in root_node.children:
    if child.products:
        print(child.products)
    else:
        print(None)
    for el in child.children:
        if el.products:
            print(el.products)
        else:
            print(None)
        for item in el.children:
            if item.products:
                print(item.products)
            else:
                print(None)
"""
