# dictionary is like object in javascript
user = {
    "key": "value",
    "name": "Mahabeer",
    "age": 30,
    "education":["BSC(I.T)", "Software engineering", "MCA"],
    "address": {
        "city":"Delhi",
        "country":"India"
    }
}

print(user["name"])
print(user["education"])

user["education"].append("Phd")

for i in user["education"]:
    print(i, end=" ")

print(user)

# to get the value of nested object
print(user["address"]["country"])

# prints all the upper layer keys
print(user.keys())


# prints all the upper layer values
print(user.values())


# prints all the object in key value pair using tuple
print(user.items())


# prints all the upper layer values
print(list(user.items()))

# through error if data is not avalaible
# print(user["school"])


# does not through error and print None instead
print(user.get("school"))


# to update new key value in dictionary
new_dic = {
    "IsAuthorized": True
}
print(user.update(new_dic))