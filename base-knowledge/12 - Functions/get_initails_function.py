def get_initial(name):
    return name[0:1].upper()


first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

print('Your initial name is ' + first_name_initial)