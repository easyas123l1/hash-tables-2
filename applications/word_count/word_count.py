def word_count(s):
    cache = {}
    invalid = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\',
               '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for x in invalid:
        s = s.replace(x, '')
    s = s.lower()
    s = s.split()
    for word in s:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
