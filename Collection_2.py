"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""



with open('text.txt', 'r') as file:
    text = file.read()

words = text.split()

count_word = {}
 
for word in words:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] =1

n = 10
sorted_words = (sorted(count_word.items(), key= lambda item: item[1],reverse=True)[:n])

print(sorted_words)
    