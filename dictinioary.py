dictionary = { "population" : 321, "dondurma": 3232323, "somthng" : 2233, "blabla" : 3344 }

pop = dictionary ["population"]
print(pop)
del dictionary["dondurma"]


print(dictionary.get("population") )

print(dictionary.items())

print(dictionary.keys())

dictionary.pop("population") #remove key-value pair

print(dictionary.keys())

print(dictionary.popitem())
#returns, as a tuple, the key-value pair that was last added to the dictionary. The method also removes the key-value pair from the dictionary

dictionary.values()
#values method: returns all the dictionaries values as a sequence

dic = { "hey" : "rere", "mehmet" : "nabiyon"}

new_div = dic | dictionary

print(new_div)

dictionary.clear() #clear everything

populations = {'New York': 8398748, 'Los Angeles': 3990456, 'Chicago': 2705994, 'Houston': 2325502, 'Phoenix': 1660272, 'Philadelphia': 1584138}

largest = {k:v for k,v in populations.items() if v > 2000000}
print(largest)

