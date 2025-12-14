my_dict = {"apple":30,"banana":35,"mango":70,"cherry":18}

asc_val = my_dict.values()
print("ascending value: ",sorted(asc_val))

desc_val = sorted(asc_val,reverse=True)
print("descending value: ",desc_val)

