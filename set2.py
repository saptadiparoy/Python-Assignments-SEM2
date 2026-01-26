#1. create two sets
a = {1,2,3,4,5}
b = {2,4,6,8,10}

#1.1 ACCESS
for element in a:
    print(element , end ="")
    print()
print("created set 1: ", a)

print("created set 2: ", b)

#2. union
unionset = a.union(b)
print ("union of sets is:   ", unionset)

#3. intersection 
interset = a.intersection(b)
print ("intersection of sets is:    ", interset)

#4. difference 
diffset1 = a.difference(b)
print ("Difference of set 1-2: ", diffset1)

diffset2 = b.difference(a)
print ("Difference of set 2-1: ", diffset2)
