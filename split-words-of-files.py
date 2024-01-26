fname = input("Enter file name: ")
try:
    fh = open(fname)
    lst = list()

    for line in fh:
        lst0 = line.split()
        for word in lst0:
            if word not in lst:
                lst.append(word)
    
    lst.sort()
    print(lst)

    fh.close()
except FileNotFoundError:
    print("File not found.")
