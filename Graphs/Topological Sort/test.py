from collections import defaultdict, deque

l = defaultdict(list)

l[0] = 2
l[2] = 3
l[2] = 4
print(l)

words = ["adv", "des", "grd", "scs", "ssds"]
for first_word, second_word in zip(words, words[1:]):
    # for c, d in zip(first_word, second_word):  # compares each letter of the words
    #     print(c, d)
    ...

for c, d in zip(words[0], words[1]):  # compares each letter of the words
    print(c, d)
else:
    print("heheheh")

