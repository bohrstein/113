set = set()
people = {"Jay", "Idrish", "Archi"}
sequence = [2, 3, 4, 5]
set.add("element")
set.update(sequence)
set.remove("item")
set.discard("item") #doesnt return error
set.clear()

for "item" in set:
    item = True

#set1.union(set2)
# set1 | set2
#set1 & set2
#set1 - set2

# Set A is subset of set B if all the elements in set A are included in set B
#setA.issubset(setB)
#setA <= setB
#Serialize an object: convert the object to a stream of bytes that can easily be stored in a file 

#Format: pickle.dump(object, file)
#Close the file
#You can pickle multiple objects to one file prior to closing the file
#Unpcikling:
#Call the pickle.load function
#Format: pickle.load(file)
