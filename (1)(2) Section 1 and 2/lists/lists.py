my_variable = 'hello'
my_list_variable = ['hello', 'hi', 'nice to meet you']
my_tuple_variable = ('hello', 'hi', 'nice to meet you')
my_set_variable = {'hello', 'hi', 'nice to meet you'}

print(my_list_variable)
print(my_tuple_variable)
print(my_set_variable)

my_short_tuple_variable = ('hello',)
another_short_tuple_variable = 'hello',
print(my_short_tuple_variable)

#-----

print(my_list_variable[0]) # called subscript
print(my_tuple_variable[0])
# print(my_set_variable[0])

my_list_variable.append('another string')
print(my_list_variable)

# my_tuple_variable.append('something')
# print(my_tuple_variable)

my_tuple_variable = my_tuple_variable + ('another string',)
print(my_tuple_variable)

my_set_variable.add('another string')
print(my_set_variable)
