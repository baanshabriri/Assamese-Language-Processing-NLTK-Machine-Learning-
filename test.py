from english_to_assamese import english_to_assamese
from reduce_word_list_size import reduce_word_list_size
word_list = []
with open("") as file:
    for line in file:
        word_list.append(line)
some_words = []
word = ""
sentence = []
flag = 0
letters = input("Enter letters:")
while letters != 'exit':
    if (letters == " " or letters == "\t"):
        sentence.append(str(word.strip()))
        word = ""
        flag = 0

        print("Sentence = ", end ='')
        for x in sentence :
            print(x + " ", end = '')
        print("\t")

    else:
        word += english_to_assamese(letters)