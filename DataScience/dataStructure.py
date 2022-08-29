'''
This file gives intorductions to python data stuctures.
Each segment in separated with #=====================
Make sure to uncomment the print functions and run the code as you move along the code to understand how python reacts to the changes.

Topics:
1. Counter
2. Lambda function
3. List
4. Dictionary
5. Default Dictionary
6. Set
'''

#===============================================================
# counter method to count frequencies of an element in the list 

from collections import Counter
age = [22,22,25,25,30,23,24,26,24,35]

value_counts = Counter(age)
common_age = value_counts.most_common()

# print(value_counts)
# print(common_age)




#===========================================================================
#anonymous finctions in Python with lambda keyword
add = lambda x,y: x+y
# print(add(10,2))




#===========================================================================
# Lists in python
# This creates the list
depths = [0, 1, 2, 3, 4, 5, 6, 7]

# This outputs the first 5 elements. No number before the : implies 0
first_5_depths = depths[:5]

# print("---0---")
# print(first_5_depths)

# You can easily sum
# print("---1---")
# print(sum(depths))

# And take the max
# print("---2---")
# print(max(depths))

# Slicing with a negative starts from the end, so this returns the last element
# print("---3---")
# print(depths[-1])

# This returns the end of the list starting from the second to the end
# Nothing after the : implies the end of the list
# print("---4---")
# print(depths[-2:])

# This returns the second, third, and forth elements
# Remember counting starts at zero!
# print("---5---")
# print(depths[2:5])

# These commands check if a value is contained in the list
# print("---6---")
# print(22 in depths)
# print(1 in depths)

# This is how you add another value to the end of your list
# depths.append(44)
# print("---7---")
# print(depths)

# You can extend a list with another list
depths.extend([100, 200])
# print("---8---")
# print(depths)

# You can also modify a value
# This replaces the 4th value with 100
depths[4] = 100
# print("---9---")
# print(depths)

# Or you can do insert to accomplish the same thing
depths.insert(5, 1000)
# print("---10---")
# print(depths)





#==============================================================================
# Dictionaries in Python

# Initialize the dictionary.
# Keys are first then a : then the value
my_dict = {"age": 22, "birth_year": 1999, "name": "jack", "siblings": ["jill", "jen"]}

# Get the value for the key age
# print("---0---")
# print(my_dict['age'])

# Check is age is a key
# print("---1---")
# print('age' in my_dict)

# Check is company is a key
# print("---2---")
# print('company' in my_dict)

# Get the value for they key age
# print("---3---")
# print(my_dict.get('age'))

# Get the value for they key company
# If it doesn't exsist, return 1
# print("---4---")
# print(my_dict.get('company', 1))

# Return all the keys
# print("---5---")
# print(my_dict.keys())

# Return all the values
# print("---6---")
# print(my_dict.values())

# Return all the key, value pairs
# print("---7---")
# print(my_dict.items())

#========================================================================
# Default Dictionary in python collections

from collections import defaultdict  # import defaultdict class
my_default_dict = defaultdict(int)   # make a default dictionary
my_default_dict['age'] = 22          # adding a key-value pair
# print(my_default_dict['company'])    # printing the value of the key "company"

#========================================================================
# Sets in Python
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(1)
# Note that the set only contains a single 1 value
# print("---0---")
# print(my_set)

my_set2 = set()
my_set2.add(1)
my_set2.add(2)
my_set2.add(3)
my_set2.add(4)
# print("---1---")
# print(my_set2)

# Prints the overlap
# print("---2---")
# print(my_set.intersection(my_set2))

# Prints the combination
# print("---3---")
# print(my_set.union(my_set2))

# Prints the difference (those in my_set but not my_set2)
# print("---4---")
# print(my_set2.difference(my_set))
