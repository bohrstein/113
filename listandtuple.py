# list is mutable tuğle is not mutable

# list can hold more than one and different tyoe data

list = [1 , "23" , "abc "]

print(list[0])
print(list[1])
print(list[2])
print(list)

print(list[-1], list[-2])
# The indexes of list start with 0 

length_of_list = len(list)


#slicing

print(list[1,2])

#list(,2) = list(0,2)


if "23" in list:
    print("everything is okay")
else:
    print("sorry")

list.append("something in my ass")

print(list[3])

print(list.count(1))

index = list.index("23")

print(index)

list.insert(2, "item")

print(list)

list.remove("23")

list.reverse()

del list[0]


list_1 = [ 0, 1, 2, 3, 4]

list_2 = [item**2 for item in list_1]

my_tuple = (1,2,3) # immutable

#processing tuple is faster than list
