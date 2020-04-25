import sys
file=open(sys.argv[1],"r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]+=1
file.close()
print('%-30s %s'% ('words','count'))
for key in wordcount.keys():
    print('%-30s %d' % (key,wordcount[keys]))
