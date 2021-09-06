# llist = ['first', 'second', 'third']
# print(llist)
#
# print()
#
# # adding elements
# llist.append('fourth')
# llist.append('fifth')
# llist.insert(3, 'sixth')
# print(llist)
# print()
#
# llist.remove('second')
# print(llist)
# print()


llist=[1,2,3,4,5,11,2,6]
print(llist)
print([id(i) for i in llist])
llist.append(4)
print(llist)
llist.insert(4,2)
print(llist)
llist.remove(2)

print(llist)

list=[1,2,3,4,5,1]
print(list)
print([id(i) for i in list])
