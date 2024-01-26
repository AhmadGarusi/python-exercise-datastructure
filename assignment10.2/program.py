fname = '/home/dale/university/python-learning/assignment9.4/mbox-short.txt'

counts = dict()
listCounts = list()

with open(fname) as fh:
    for line in fh:
        words = line.split()
        if not words or words[0] != 'From':
            continue
        else:
            hour = words[5].split(':')
            counts[hour[0]] = counts.get(hour[0], 0) + 1

listCounts = counts.items()
listCounts = sorted(listCounts)

for x,y in listCounts:
    print (x,y)