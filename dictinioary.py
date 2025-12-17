dictionary = { "population" : 321, "dondurma": 3232323 }

pop = dictionary ["population"]
print(pop)
del dictionary["dondurma"]

dictionary.clear() #clear everything

dictionary.get("population") 

dictionary.items()

dictionary.keys()

dictionary.pop("population") #remove key-value pair

dictionary.popitem()
#returns, as a tuple, the key-value pair that was last added to the dictionary. The method also removes the key-value pair from the dictionary

dictionary.values()
#values method: returns all the dictionaries values as a sequence

dic = { "hey" : "rere", "mehmet" : "nabiyon"}

new_div = dic | dictionary
