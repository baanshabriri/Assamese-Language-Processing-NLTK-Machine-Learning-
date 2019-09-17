from nltk.tokenize import word_tokenize
import string


with open('/Users/partha/All/Python/ProjectMaterials/Learned material/Arts/Psychology.txt', encoding='utf-16') as content_file:
    content = content_file.read()

content = word_tokenize(content.replace('।', '.'))

content_length = len(content)
i = 0
while i < content_length:
    for c in string.punctuation:
        content[i] = content[i].replace(c, "")

    if content[i] == '':
        content.pop(i)
        content_length -= 1
    i += 1


print(content)

total_words = len(content) -1                           #   total number of words
counter1 = 0                                            #   counter for the first method
counter2 = 0                                            #   counter for the second method

for i in range (0, total_words):
    next_word_list_5 = function_1(content[i])           #   1st function call that returns a list of 5 predicted words

    if content[i+1] in next_word_list_5:
        counter1 += 1

for i in range(0, total_words):
    next_word_list_5 = function_2(content[i])           #   2nd function call that returns a list of 5 predicted words

    if content[i + 1] in next_word_list_5:
        counter2 += 1



success_rate_1 = (counter1/total_words)*100
success_rate_2 = (counter2/total_words)*100

print(success_rate_1+'%')                               #   success rate of 1st method
print(success_rate_2+'%')                               #   success rate of 2nd method



