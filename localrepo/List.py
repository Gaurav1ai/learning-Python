List1 = ["apple","banana","cherry"]
List2 =["a","b","c","d","e","c"]
# #Acccessing List 
# print(List1[0])
# print(List1[1])
# print(List1[2])
# print(List1[-1])
# print(List1[-2])
# print(List1[-3])

# print(List2[2:5])
# print(List2[-4:-1])

# #find element is exist or not in the list
# if "a" in List2:
#     print("a is present in List2")
    
# #changing Liat items
# List2[2]=List1[0]
# print(List2)
# List2.insert(2,'jbl')
# print(List2)

# #add list in another list
# List1.extend(List2)
# print(List1)

# #add specific element
# List2.append("f")
# print(List2)

# #add specific element at specific position
# List2.insert(1,"f")
# print(List2)

# #remove any elemnt
# List2.remove("f")
# print(List2)

# # remove specific elemnt by index using pop
# List2.pop()
# List2.pop(2)
# print(List2)

# #using del keyword to delete
# del List2[0]
# print(List2)
# del List1
# print(List1) #It give Compile error  that List1 is not define

# #Use of Clear
# List1.clear()
# print(List1) #It clear list elements not delete list

##Write a program in which if a specific element find in the list then remove that specific element if not then clear the list 
# target= input("Enter the element to remove: ")

# le =len(List2)

# if target in List2:
#     List2.remove(target)
#     print(List2)
# else:
#     List2.clear()
#     print(List2)
    
# if target in List2:
#     del List2
#     print(List2)

