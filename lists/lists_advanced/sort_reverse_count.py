# count() method
# The count() method returns the number of times a value occurs in a list. If the value is not in the list, it returns '0'

import numbers


language = ['C#', 'C#','C','PHP', 'Python', 'Java', 'JavaScript']

print(language.count('C#'))

# reverse() method reverses a list in-place that is it doesn't make a new copy of the list but rather rearrange the list in reverse order in the same container/list/data structure

nums = [1,2,3,4,5,6,7,8]

nums.reverse()
print(nums)


# sort() method arrange list elements in an ascending (least to greatest) order

numbers = [8, -2, 4, -9, 3, 1, -4, 5, 4]

numbers.sort()

print(numbers)