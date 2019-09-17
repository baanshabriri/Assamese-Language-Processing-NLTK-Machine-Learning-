from nltk.tokenize import word_tokenize

stop_words_list = open("/Users/partha/All/Python/ProjectMaterials/StopWords.txt", 'r', encoding='utf-16')
stop_words = word_tokenize(stop_words_list.read())

example_text = "১৩ শতিকাৰ পৰা ঊনৈশ শতিকাৰ প্ৰথমছোৱালৈকে অসমত আহোমসকলে ৰাজত্ব কৰিছিল । এই ৰাজবংশৰ প্ৰতিষ্ঠাতা আছিল চুকাফা । তেওঁ চীনৰ য়ুনানৰ ওচৰৰ মাওলুং ৰাজ্যৰ পৰা আহিছিল । এটা ৰাজপৰিয়ালৰ লোকে এইদৰে সুদীৰ্ঘ ছশ বছৰ ৰাজত্ব কৰাৰ দৃষ্টান্ত বিৰল ।".replace("।", ".")
words = word_tokenize(example_text)


filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)