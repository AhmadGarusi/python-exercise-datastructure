fname = '/home/dale/university/python-learning/assignment9.4/mbox-short.txt'
senders = dict()
count = 0
words = list()

with open(fname) as fh:
    for line in fh:
        words = line.split()
        if not words or words[0] != 'From':
            continue
        if words[1] in senders:
            senders[words[1]] += 1
        else:
            senders[words[1]] = 1

bignum = 0

for k in senders:
    if senders[k] > bignum:
        bignum = senders[k]
        bigname = k
print (bigname, bignum)