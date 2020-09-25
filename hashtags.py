import re
filename = "lib.txt"
fh = open(filename)
print('Reading all hashtags from : '+ filename)
counts = dict()
templist = list()
sortlist = list()
total = 0
for line in fh:
    templist = re.findall('#\S+',line)
    for words in templist:
        total += 1
        counts[words] = counts.get(words,0)+1
for k,v in counts.items():
    sortlist.append((v,k))
sortlist = sorted(sortlist, reverse = True)

print('Total count of Hashtags read from the file is :' , total)
print('Best 30 Hastags for your post will be :-')
for v,k in sortlist[:30]:
    print(k,end=' ')

#print(sorted([(v,k) for k,v in counts.items()],reverse =True))