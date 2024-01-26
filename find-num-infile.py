# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s += float(line[19:])
    count = count + 1

print("Average spam confidence:", s/count)
