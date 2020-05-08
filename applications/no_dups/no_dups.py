def no_dups(s):
    # Implement me.
    # hash
    # cache = {}

    # split string
    # li = list(s.split(" "))

    # for i in s:
    #     # check if word is a word
    #     if i.isspace():
    #         continue

    #     if i not in cache:
    #         cache[i] = 1
    #     else:
    #         cache[i] += 1
    # return cache

    li = s.split(" ")

    return set(li)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
