# from Dan at Real Python
# PyTricks


my_list = ['click', 'click', 'boom']
print('My list: {}'.format(my_list))
# delete the entire list
del my_list[:]
print('My list: {}'.format(my_list))

my_boss_list = ['Russ', 'Mark', 'Steve', 'Brian', 'Crystal', 'Me!']
print("My Boss List: {}".format(my_boss_list))

boss_count = 0
for mbl in my_boss_list:
    if mbl == 'Me!':
        pass
    else:
        boss_count += 1

print("Jim has {} bosses righ now, but hard work will pay off!".format(
    boss_count))

