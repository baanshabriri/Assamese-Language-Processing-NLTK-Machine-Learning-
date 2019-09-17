word_list = []
with open("/Users/partha/All/Python/ProjectMaterials/Stemming/dict.txt", encoding='utf-8') as file:
    for line in file:
        word_list.append(line)

def assamese_word_selector_I(letters):
    i = 0
    probable_words = []

    for word in word_list:
        if word.startswith(letters) and i<5:
            print(str(i+1)+'\t'+word)
            probable_words.append(word)
            i = i+1

    choice = input("Enter choice :")

    return probable_words[int(choice)-1]

print(assamese_word_selector_I('ক'))
# print(assamese_word_selector_I("দেহ"))
# print(assamese_word_selector_I("ধাৰ"))
# print(assamese_word_selector_I("নিগ"))