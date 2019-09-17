def reduce_word_list_size(word_list, letters):
    i = 0
    for word in word_list:
        if word.startswith(letters):
            word_list[i] = word
            i += 1

    return word_list[:i]
