import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def token_assamese():
    # Modifiy these to change the location of the coupus file  and the name of  the courpus  file
    corpus_path = "/Users/partha/All/Python/ProjectMaterials/Learned material/Arts"
    corpus_filename = 'Psychology.txt'

    newcorpus = PlaintextCorpusReader(corpus_path, corpus_filename, encoding='utf16')
    text =  newcorpus.raw().strip().replace('।','.')
    words = nltk.word_tokenize(text)

    for index, item in enumerate(words):
        if (str(item) == '.'):
            words[index] = '।'

    output_file_path = "C:/Users/HEMANT/Documents/1.Project/"
    output_filename = 'Result.txt'

    with open(output_file_path + output_filename, 'w', encoding='utf8') as f:
        for i in words:
            f.writelines(str(i)+'\n')

    f.close()

token_assamese()