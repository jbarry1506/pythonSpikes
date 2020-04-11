# from Dan at Real Python
# PyTricks
import pprint

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

try:
    for mb in my_boss_list:
        print(mb)
except:
    print("There is somethhing fishhy going on here.")

def boss_switch(self, ls):
    the_list = []
    dict_add = {}
    count = 0
    for i in ls:
        if i in ls:
            print('{} is already in the list!')
        else:
            count += 1
            dict_add += {
                count: i
            }
            the_list.append(dict_add)
            count += 1

    return the_list


try:
    boss_switch()
    for num_boss in my_boss_list:
        pprint.pprint(num_boss)
        
except:
    pass
