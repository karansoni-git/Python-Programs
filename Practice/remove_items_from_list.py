list1 = ['a','b','c','d','e','f','g','h']

remove_list = [0,2,3,5]

updated_list = [item for idx, item in enumerate(list1) if idx not in remove_list]

print(updated_list)
