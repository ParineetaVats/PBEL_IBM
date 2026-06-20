my_list=[1,2,3,4]
print(my_list)
print(type(my_list))
#List
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))


#Methods
print(len(my_list))


my_list.append(6)  # is used to add an element to the end of the list
print(my_list)


my_list.insert(0, 0)  # is used to add an element at a specific index
print(my_list)  


my_list.extend([7, 8, 9])  # is used to add multiple elements to the end of the list
print(my_list)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b                              # letters in a but not in b

a | b                              # letters in a or b or both

a & b                              # letters in both a and b

a ^ b                              # letters in a or b but not both

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

tel['irv']
print(tel.get('irv'))

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel