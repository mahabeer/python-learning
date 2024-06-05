# set is a collection of unordered list
# each element in the set must be unique and immutable

nums = {1,2,3,4,5,3,2}

# remove duplicates and print unique values
print(nums)

# to create empty set
collection = set()

# to add & remove value in set
nums.add(12)
nums.remove(3)
nums.pop()
print(nums)


# to copy a set in new variable
newset = nums.copy()
nums.add(11)
nums.add(13)

print('newset',newset)
# to clear set
nums.clear()
print(nums)


set1 = { 1,2,3,5}
set2 = { 1,2,7,8}

unique_set = set1.union(set2)
print(unique_set)

common_set = set1.intersection(set2)
print(common_set)