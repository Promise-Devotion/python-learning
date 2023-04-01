def get_initial(name, force_upper):
    if force_upper:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("请输入你的名字：")
first = get_initial(first_name, True)

print(first)
