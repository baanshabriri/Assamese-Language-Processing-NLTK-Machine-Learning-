from english_to_assamese import english_to_assamese

word_list = []
with open("/Users/partha/All/Python/ProjectMaterials/Stemming/dict.txt", encoding='utf-8') as file:
    for line in file:
        word_list.append(line)


def assamese_word_selector_II(letters):
    i = 0
    probable_words = []

    for word in word_list:
        if word.startswith(letters) and i < 5:
            print(str(i + 1) + '\t' + word)
            probable_words.append(word)
            i = i + 1

    print("6\tNone")

    choice = input("Enter choice :")
    if int(choice) != 6:
        return probable_words[int(choice) - 1]
    elif int(choice) == 6:
        return


word = ""
selected_word = ""
sentence = []

letter = input("Enter letters (type \"exit\" to exit) :")
while letter != 'exit':
    if(letter == " " or letter == "\t"):
        sentence.append(selected_word)
        selected_word = ""
        word = ""

    else:
        word = word+english_to_assamese(letter)
        selected_word = assamese_word_selector_II(word)
        if selected_word == None:
            print("Selected word = "+str(word))
        else:
            print("Selected word = "+str(selected_word))

    x = ""
    if selected_word == None:
        x = word
    else:
        x = selected_word

    letter = input("Enter letters (type \"exit\" to exit, space for new word):\nPrevious input = "+str(x)+"\n")
    if(letter == "exit"):
        sentence.append(selected_word)

print(sentence)