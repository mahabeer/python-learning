fruits = ["Orage", "Apple", "Banana"]
print( fruits )

# to add item in list at last
fruits.append("Grapes")

# to add multiple items on list
fruits.extend(["Kiwi","Watermelon"])


# to remove elements from list from last default
fruits.pop()
# remove from 2nd index
fruits.pop(2)
# remove based on value
fruits.remove("Kiwi")

# to clear a list
# fruits.clear()

# count method to get the occurance of an item
fruits.count("Kiwi")


# to sort the list
fruits.sort()
print( fruits )


# insert an element at particular index
fruits.insert(1, "New fruite")
fruits[0]="abc" # list is mutable
print(fruits)


# Tuples : Immutable data types
marks = (32,43,54,64,32)
print(marks[2])


# prints index of a tuple value
marks.index(43)

# returns occurance of value
print(marks.count(32))

movies = []
mov1= input("Enter 1st movie")
mov2= input("Enter 2nd movie")
mov3= input("Enter 3rd movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
