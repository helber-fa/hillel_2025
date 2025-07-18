def get_5():
    return 5

print(get_5())
print(get_5)

new_get_5 = get_5

print(new_get_5())
print(id(get_5))
print(id(new_get_5))

list_string = ["atbt", "htaatt", "tttpt", "tsssqsq"]

wrd = ''
max_t = 0
for k in list_string:
    if k.count("t") > max_t:
        wrd = k
        max_t = k.count("t")

def get_word_with_max_letter(letter, list):
    wrd = ''
    max_t = 0
    for k in list:
        if k.count(letter) > max_t:
            wrd = k
            max_t = k.count(letter)
    return wrd

def count_t(word):
    return word.count("t")

print(wrd)
print(max_t)

print(get_word_with_max_letter("t", list_string))
print(max(list_string, key=count_t))

print(max(list_string, key=lambda x: x.count("t")))


