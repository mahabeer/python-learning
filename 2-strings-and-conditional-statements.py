# len() method to get the length of the string
name="Mahabeer Singh"
print(len(name))

# [index] indexing of a string
print(name[2])

# getting last letter of string
lastLetter = name[len(name)-1]
print(lastLetter)

# slicing Mahabeer to ah, starts from 1 and till 2nd index
print(name[1:3])

# slicing using minus index, Mahabeer to ah, starts from 1 and till 2nd index
print(name[-7:-5])

# String functions endswith
print(name.endswith("er")) #True
print(name.endswith("ab")) #False

# String functions upper() & lower() for uppercase/lowecase a string
print(name.upper()) #MAHABEER
print(name.lower()) #mahabeer

# String replace method to replace the string
print(name.replace("Mahabeer","Vikas"))

# String replace method to replace the string
print(name.find("Singh"))

# String count method to get the occurance of particular char
print("Occurance of M is : ",name.count("a"))

# exsercise : input name from user and print its length
# username = input("Enter your name : ")
# print(len(username))

# conditional statements if, elif, else
age = 17
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

light = "yellow"
if(light == "green"):
    print("You can drive")
elif(light == "yellow"):
    print("You need to wait")
else:
    print("You need to stop")

studentMarks= int(input("Enter your marks : "))

if(studentMarks >=90):
    studentGrad="A"
elif(studentMarks>=80 and studentMarks < 90):
    studentGrad="B"
elif(studentMarks>=70 and studentMarks < 80):
    studentGrad="C"
else:
    studentGrad="D"

print('studentGrad: ',studentGrad)

# check if number is even or odd
isEven= int(input("Enter your number : "))
if(isEven % 2 == 0):
    print("Its even number")
else:
    print("Its odd number")