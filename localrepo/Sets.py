set1={"a","b","c","d"}
set2={1,2,3,4,5,6}
set3={"jhon","banana","kiwi"}
i=(7,8,9,0,11)

set1.add("e")
print(set1)

set4 = set1.update(set2)
print(set4)


set1.remove("e")
print(set1)

set5 = set2.discard(4)
print(set5)

set6=set3.pop()
print(set6)

# set5.clear()
print(set5)

set5 = set1.union(set3)
print(set5)

# set6.clear()
set6=set1|set2
print(set6)

newset=set1.union(i)
print(newset)


# print(set1)
# print("banana" in set1)
# print("banana" not in set1)