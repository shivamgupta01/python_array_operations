# Testing out different Operations in Array. 

# Initializing 1-d array.
nums = []
print(nums)
print('*********************************')

# Initializing List with Values.
nums = [1,2,3,4,5]
print(nums)
print('*********************************')

# Initializing List with multiple data structure. 
nums = [1,2,3,'four','five','six']
print(nums)
print('*********************************')

# Initializing a 2-d List
nums = [[1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
        ]
print(nums)
print('*********************************')

# Iterating through List.
# 1. Enhanced For loop

nums = [1,2,3,4,5]
for item in nums:
        print(item)
print('*********************************')

# Finding out length of List.
print(len(nums))
print('*********************************')

# Iterating through list with range
for i in range(len(nums)):
        print(nums[i])
print('*********************************')

# Append a List, equivalent to nums[len(nums):] = [item]
nums.append(6)
# or
nums[len(nums):] = [7]
print(nums)
print('*********************************')

# Add another iterable to a List. Can use + operator instead of extend
print(nums+['one','two','three','four','five','six','seven'])
print(nums)
print('*********************************')
# or
nums.extend(['one','two','three','four','five','six','seven'])
print(nums)
print('*********************************')

# Inserting at specific location.
# nums.insert(arg1,arg2)
# arg1 = index at which the value is to inserted.
# arg2 = value to be inserted. 
nums.insert(14,8)
print(nums)
print('*********************************')

# Removing element from List.
# .remove(x) will remove the first element from the list. 
# If the element is not found "ValueError" is raised. 

nums.remove(8)
try:
        nums.remove(14)
except ValueError as exception:
        print("Exception occurred while removing item: " + str(exception))

print('*********************************')

# pop([i]) also removes an element from the list and returns it. 
# If no index is specified then the last element is removed.

print(nums.pop())
print(nums.pop(0))
try:
        print(nums.pop(111))
except IndexError as exception:
        print("Exception Occurred: " + str(exception))
print('*********************************')

# .clear will clear the while list.
# Uncommon it.
# nums.clear()
print(nums)
print('*********************************')

# Finding the index of a given element 
# .index(x)
# ValueError is raised if no such element is found. 
print(nums.index(2))
print('*********************************')

# Counting the occurrence of a given element.
print(nums.count(2))
print('*********************************')

# Reversing an List
nums.reverse()
print(nums)
print('*********************************')

# Sorting an List
nums = [3,2,4,6,7,8,1]
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)
print('*********************************')