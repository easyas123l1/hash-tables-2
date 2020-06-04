

def word_count(s):

    cache = {}
    invalid = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\',
               '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for x in invalid:
        s = s.replace(x, '')
    s = s.lower()
    s = s.split()
    for letter in s:
        if letter in cache:
            cache[letter] += 1
        else:
            cache[letter] = 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
