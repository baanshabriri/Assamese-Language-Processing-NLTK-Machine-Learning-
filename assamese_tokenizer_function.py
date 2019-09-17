from nltk.tokenize import word_tokenize

def assamese_tokenizer(word_list):
    word_list2 = []
    for i in range(len(word_list)):
        for j in word_tokenize(word_list[i]):
            word_list2.append(j.replace(".", "।"))

    return word_list2
