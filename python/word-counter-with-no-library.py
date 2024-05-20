# This requires 0 dictonaries
sentence = input("Enter a word or sentence: ")

sentence = sentence.replace(",", "").lower().split()
wc = {}

for word in sentence:
    if word in wc.keys():
        wc[word] += 1
    else:
        wc[word] = 1


print(wc)
