fname = '/home/dale/university/python-learning/assignment8.3/mbox-short.txt'

count = 0

with open(fname) as fh:
    for line in fh:
        words = line.split()
        if words[0] != 'From':
            continue
        count += 1
        print(words[1])

print("There were", count, "lines in the file with From as the first word")