#Program to print the most occuring word in a file
fname =input('Enter the file name:')
fh = open(fname)
counts = dict()
for line in fh:
    line = line.strip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print(counts)
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword,bigcount)
