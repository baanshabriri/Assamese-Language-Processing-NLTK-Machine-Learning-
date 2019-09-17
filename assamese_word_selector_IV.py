from english_to_assamese import english_to_assamese
from reduce_word_list_size import reduce_word_list_size

word_list = []
with open("C:\Python 3.6\ProjectMaterials\Stemming\dict.txt", encoding='utf-8') as file:
    for line in file:
        word_list.append(line)


some_words = []
#********************************************************************#
def assamese_word_selector_IV(letters, flag):
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
        return probable_words[int(choice) - 1].strip()
    else:
        return letters.strip()

# ******************************************************************** #

word = ""
sentence = []
flag = 0
letters = input("Enter letters (type \"exit\" to exit) :")

while letters != 'exit':
    if (letters == " " or letters == "\t"):
        sentence.append(str(word.strip()))
        word = ""
        flag = 0

        print("Sentecte = ", end='')
        for x in sentence:
            print(x + " ", end='')
        print("\t")

    else:
        word += english_to_assamese(letters)
        word = assamese_word_selector_IV(word, flag)
        flag = 1
        # print("Selected word = " + str(word))

        print("Sentecte = ", end='')
        for x in sentence:
            print(x + " ", end='')
        print("\t"+word)


    letters = input("Enter letters (type \"exit\" to exit, space for new word):"+ "\n") #\nPrevious input = " + str(word) + "\n")
    if (letters == "exit"):
        sentence.append(str(word.strip()))


#********************************************************************#

print("Final sentece = ", end='')
for word in sentence:
    print(word+" ", end='')
print('|')