my_dict={
    "name":"ford",
    "age" : 21,
    "proffession" : "Developer"
}

# print(my_dict)


# Access items
x = my_dict["proffession"]
y= my_dict.get("age")
z = my_dict.keys()
print(y)
print(x)
print(z)

# update dictionary
my_dict.update({"age":30})
print(my_dict)
my_dict["name"]="Gaurav"
print(my_dict)

# Add items
my_dict["color"]= "red"
print(my_dict)

my_dict.update({"Mood": "Anger"})
print(my_dict)

#Remove items

my_dict.pop("color")
print(my_dict)

my_dict.popitem()
print(my_dict)
del my_dict["name"]
print(my_dict)