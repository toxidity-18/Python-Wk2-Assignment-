# Creating an empty list .
my_list = []
# appending/adding elements inside my list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# insert value 15 at the second position in the list .
my_list.insert(1,15)
print(my_list)
# extending extra elements 
another_list=[50,60,70]
my_list.extend(another_list)
print(my_list)
# Remove the last element inside my list 
# del my_list[-1]: deleting an element 
my_list.remove(70)
print(my_list)  
# sort my_list in ascending order .
my_list.sort()
print(my_list)
# print out the index of value 30 
index_of_30 = my_list.index(30)
print(index_of_30)
# print(my_list[3]) : confirmation .
