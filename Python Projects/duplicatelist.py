lst = [1,2,3,4,2,5,1,6,7,1,11,9,10,2,4,1,5,3,1]
for i in lst:
    for j in range(lst.index(i)+1,len(lst)+1):
        if i == j:
            print("\t{} IS PRESENT MULTIPLE TIMES".format(i))
            print("\tNUMBER OF OCCURENCES OF THE ELEMENT {}: {}".format(i,lst.count(i)))
        else:
            continue
