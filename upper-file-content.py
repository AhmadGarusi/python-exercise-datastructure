fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.upper()
    line = line.rstrip()
    print(line)