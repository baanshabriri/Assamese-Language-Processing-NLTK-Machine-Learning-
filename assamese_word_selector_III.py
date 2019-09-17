from english_to_assamese import english_to_assamese
from reduce_word_list_size import reduce_word_list_size


word_list = []
with open("/Users/partha/All/Python/ProjectMaterials/Stemming/dict.txt", encoding='utf-8') as file:
    for line in file:
        word_list.append(line)

some_words = []


#********************************************************************#
def assamese_word_selector_III(letters, flag):
    global some_words
    probable_words = []
    i = 0

    if flag == 0:
        some_words = reduce_word_list_size(word_list, letters)

    elif flag == 1:
        some_words = reduce_word_list_size(some_words, letters)

    for word in some_words:
        if i < 5:
            print(str(i + 1) + '\t' + word)
            probable_words.append(word)
            i = i + 1

    print("6\tNone or "+letters)

    while True:
        choice = input("\nEnter choice :")
        if choice.isnumeric():
            break
        else:
            print("Wrong input. Try again.")

    if int(choice) > 0 and int(choice) < 6 and len(probable_words)>0:
        return probable_words[int(choice) - 1]
    else:
        return letters

#********************************************************************#

word = ""
selected_word = ""
sentence = []
flag = 0

letter = input("Enter letters (type \"exit\" to exit) :")
while letter != 'exit':
    if(letter == " " or letter == "\t"):
        sentence.append(str(selected_word.strip()))
        selected_word = ""
        word = ""
        flag = 0

    else:
        # print(word)
        word = word+english_to_assamese(letter)
        # print(word)
        selected_word = assamese_word_selector_III(word, flag)
        flag = 1
        if selected_word == None:
            print("Selected word = "+str(word))
            # selected_word=word
        else:
            print("Selected word = "+str(selected_word))



    # x = ""
    # if selected_word == None:
    #     x = word
    # else:
    #     x = selected_word

    if selected_word != None:
        word=selected_word

    letter = input("Enter letters (type \"exit\" to exit, space for new word):\nPrevious input = "+str(word)+"\n")
    if(letter == "exit"):
        sentence.append(str(selected_word.strip()))
    # word=x


#********************************************************************#

print()
for word in sentence:
    print(word+" ", end='')