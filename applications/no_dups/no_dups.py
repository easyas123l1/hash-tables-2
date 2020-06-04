def no_dups(s):
    # Your code here
    cache = {}
    string = ""
    s = s.split()
    first = True
    for word in s:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
            if first:
                string += word
                first = False
            else:
                string += ' ' + word
    return string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
