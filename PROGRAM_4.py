dict1 = {2:"Orange",3:"Banana",1:"Apple"}
print(f"Dictionary 1 : {dict1}")
l = list(dict1.items())
l.sort()
print("Ascending order is :", l)
l = list(dict1.items())
l.sort(reverse=True)
print("Descending Order is :",l)
dict2 ={4:"Plum",5:"Cherry"}
print(f"Dictionary 1: {dict2}")
dict1 .update(dict2)
print(f"Dictionary after merging: {dict1}")



