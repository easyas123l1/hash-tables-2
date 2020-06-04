import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()
cacheStart = {}
cacheMid = {}
cacheEnd = {}
punctuation = ['.', '?', '!']
for i in range(len(words) - 1):
    # find if a start word (starts with "capital or capital)
    if len(words[i]) >= 2:
        if words[i][:1] == '"' + words[i][1].upper() or words[i][0] == words[i][0].upper():
            if words[i] in cacheStart:
                cacheStart[words[i]].append(words[i+1])
            else:
                cacheStart[words[i]] = [words[i+1]]
        # test word is a end word (punctuation in last or second to last spot)
        elif words[i][-1] in punctuation or words[i][-2] in punctuation:
            cacheEnd[words[i]] = words[i]
        else:
            if words[i] in cacheMid:
                cacheMid[words[i]].append(words[i+1])
            else:
                cacheMid[words[i]] = [words[i+1]]
    else:
        # copy pasta
        if words[i][0] == words[i][0].upper():
            if words[i] in cacheStart:
                cacheStart[words[i]].append(words[i+1])
            else:
                cacheStart[words[i]] = [words[i+1]]
        # test word is a end word (punctuation in last or second to last spot)
        elif words[i][-1] in punctuation:
            cacheEnd[words[i]] = words[i]
        else:
            if words[i] in cacheMid:
                cacheMid[words[i]].append(words[i+1])
            else:
                cacheMid[words[i]] = [words[i+1]]


# TODO: construct 5 random sentences

# Your code here
print(cacheStart)
print(cacheMid)
print(cacheEnd)
