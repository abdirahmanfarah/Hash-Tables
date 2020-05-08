import re


def word_count(s):
    # Implement me.
    # <!-- Turn string into dictionary -->
    # <!-- count how many words show up in the string -->
    # <!-- output is word as key, and value as the count -->
    # <!-- key is lowercase -->
    # we need a cache
    cache = {}

    li = list(s.split(' '))
    # li = re.split('" : ; , . - + = / \ | [ ] { } ( ) * ^ &', s)

    # loop through the array
    for i in li:
        # check if word is a word
        if i.isspace():
            continue

        i = i.lower()

        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1
    return cache

    # loop through string
    # for i in s:


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count(
    #     'This is a test of the emergency broadcast network. This is only a test.'))

