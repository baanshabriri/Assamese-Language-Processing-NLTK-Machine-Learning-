from assamese_tokenizer_function import assamese_tokenizer

plural = ["দল", "বোৰ", "হঁত", "সকল", "মখা", "বিলাক", "সোপা",
			"মান", "বৰ্গ", "বৃন্দ", "মণ্ডলী", "ৰাজি", "ৰাশি", "সমুহ", "আৱলী",
			"চেৰেক", "দিয়েক"]

cas = ["ক", "ত", "লৈ", "এ", "ৰ", "দ্বাৰা", "দি", "ই", "ৰপৰা",
			"পৰা", "ে"]

definitive = ["জন", "জনী", "জনা", "খন", "টো", "টা", "টি", "ডাল", "লদা", "ডালি", "গৰাকী", "জাক", "আখি", "আঁটি", "কঠা",
            "কণ", "কণি", "কাচলি", "কোছা", "কুৰা", "খন", "খনি", "খিনি", "খিলা", "খৰ", "গছ", "গছি", "গাল", "গোট",
            "গৰাকী", "ঘৰ", "চকল", "চটা", "চটি", "চপৰা", "চমকা", "চলু", "চলা", "চলি", "চাব", "চাম", "চিলিম", "চিৰা",
            "পাহি", "পাহ", "সাজ",
            "চেলেকা", "ছাটি", "ছালি", "ছোৱা", "খুতুৰা", "পাত",  "যোৰ","যুৰি", "যুগল", "হাল", "দ্বয়", "গণ্ডা", "হালি", "কোছা",
             "খিনি", "গাল", "চিৰা", "টাঁৰ", "ডৰা", "টোপা", "মুঠা", "মুঠি", "পোলা", "গছি", "ষাৰ", "মখা", "জাক", "দল", "আখি",
             "ঠোকা", "ধাৰ",  "ধাৰি", "ডোখৰ",  "ডুখৰি",  "কণ",  "কণি",  "টাঁৰি",  "ফেৰা",  "ফেৰি",  "জাউৰি",  "থোপা",  "থুপি",
              "জোপা",  "জুপি", "ডোঙা", "চাব"]

pleo = ["হে", "চোন", "নে", "ো", "ও","েই", "ৱেই", "য়েই", "ৱ", "ওক","গৈ", "না"]

extra = ["োৱে", "োঁতেই", "েৰে", "য়ে", "নো", "ভাৱে", "কৈ", "দৰে",
			"ঁহক", "ৰপৰা", "পৰা"]

indefinitive = ["এক","তো", " েক",  "কেইজন", "কেইজনী"]

ক্ৰিয়া = ["াই",  "াইছ",  "াইছা", "াইছিল", "াইছিল",  "াইছিলা",  "াইছিলি", "াইছিলোঁ",  "াইছে", "াইছোঁ",
            "াওঁ",  "াওক", "াক",  "াব", "াবলৈ",  "াবা", "াবি",  "াম", "ায়",  "াল", "ালত",  "ালা", "ালি",
            "ালে", "ালোঁ",  "াৱ",  "ি",  "িছ", "িছা",  "িছিল", "িছিলা",  "িছিলি", "িছিলোঁ",  "িছে",
            "িছোঁ",  "িব", "িবলৈ", "িবি", "িবা", "িম",  "িল",   "িলত", "িলা",  "িলি", "িলে","ে", "িলোঁ",
            "োঁ", "ো", "োৱা", " োঁৱা", "োৱাই",  "োৱাইছ", "োৱাইছা",  "োৱাইছিল",  "োৱাইছিলা",  "োৱাইছিলি",  "োৱাইছিলোঁ",
            "োৱাইছে",  "োৱাইছোঁ", "োৱাওঁ",  "োৱাওক","োঁৱাওক", "োৱাক", "োৱাব", "োৱাবলৈ",  "োৱাবা",  "োৱাবি",
            "োৱাম",  "োৱায়",  "োৱাল",  "োৱালত",  "োৱালা",  "োৱালি",  "োৱালে", "োৱালোঁ", "োৱাৱ", "িবলৈ",
            "া", "ক",   "ব", "বলৈ", "বা", "বি", "ম", "ইছ", "ইছা", "ইছিল", "ইছিলা", "ইছিলি", "ইছিলোঁ", "ইছে", "ইছে", "ইছোঁ", "ওৱা", "ওৱা",
            "য়া", "য়াই",  "য়াই",  "য়াইছ", "য়াইছ", "য়াইছা", "য়াইছা", "য়াইছিল", "য়াইছিল", "য়াইছিলা", "য়াইছিলা",
            "য়াইছিলি", "য়াইছিলি", "য়াইছিলোঁ", "য়াইছিলোঁ", "য়াইছে", "য়াইছে", "য়াইছোঁ", "য়াইছোঁ",
            "য়াওঁ", "য়াওঁ", "য়াওক", "য়াওক", "য়াক", "য়াব",  "য়াব",  "য়াবলৈ",  "য়াবলৈ",  "য়াবা", "য়াবা",
            "য়াবি", "য়াবি",  "য়াম", "য়াম",  "য়ায়", "য়ায়", "য়াল", "য়াল", "য়ালত", "য়ালত", "য়ালা", "য়ালা", "য়ালি",
            "য়ালি", "য়ালে", "য়ালে", "য়ালোঁ", "য়ালোঁ", "য়াৱ", "য়াৱ", "লত", "লা", "লি", "লে", "লোঁ"]

kinshipnouns = ["য়েক"]

arl = []

for i in range(len(plural)):
   for j in range(len(cas)):
       kit = plural[i]+cas[j]
       arl.append(kit)

for i in range(len(plural)):
   for j in range(len(pleo)):
       kit = plural[i]+pleo[j]
       arl.append(kit)

for i in range(len(definitive)):
   for j in range(len(pleo)):
       kit = definitive[i]+pleo[j]
       arl.append(kit)

for i in range(len(definitive)):
   for j in range(len(cas)):
       kit = definitive[i]+cas[j]
       arl.append(kit)

for i in range(len(indefinitive)):
   for j in range(len(plural)):
       kit = indefinitive[i]+plural[j]
       arl.append(kit)

for i in range(len(ক্ৰিয়া)):
   for j in range(len(pleo)):
       kit = ক্ৰিয়া[i]+pleo[j]
       arl.append(kit)

for i in range(len(cas)):
   for j in range(len(pleo)):
       kit = cas[i]+pleo[j]
       arl.append(kit)

for i in range(len(ক্ৰিয়া)):
    arl.append(ক্ৰিয়া[i])

for i in range(len(extra)):
    arl.append(extra[i])

for i in range(len(plural)):
    arl.append(plural[i])

for i in range(len(definitive)):
    arl.append(definitive[i])

for i in range(len(indefinitive)):
    arl.append(indefinitive[i])

for i in range(len(pleo)):
    arl.append(pleo[i])

for i in range(len(kinshipnouns)):
    arl.append(kinshipnouns[i])

for i in range(len(cas)):
    arl.append(cas[i])

dict_list = []
with open("/Users/partha/All/Python/ProjectMaterials/Stemming/dict.txt", encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        dict_list.append(line.strip())

# print(dict_list)

def stemmedToken(token):
    ct = 0
    flag = 0
    arl1 = ""
    for i in range(len(arl)):
        if(token.endswith(arl[i])):
            if (len(arl[i]) > ct):
                arl1 = arl[i]
                ct = len(arl[i])
                flag = 1

    if(flag == 0):
        return token
    else:
        return token[0:(len(token)-len(arl1))]

def isDictionaryWord(token):
    flag = 0
    for i in range(len(dict_list)):
        if(token == dict_list[i]):
            flag = 1
    return flag

def tokenClean(token):
    cstr = token.strip()

    if (token.endswith("।") or token.endswith("|") or token.endswith("?") \
                or token.endswith(",") or token.endswith("'") \
                or token.endswith("\"") or token.endswith("-") \
                or token.endswith(")") or token.endswith("(") \
                or token.endswith("\\") or token.endswith("}") \
                or token.endswith("{") or token.endswith(":") \
                or token.endswith(";") or token.endswith(".") \
                or token.endswith("?") or token.endswith("!")):
        cstr = token[0:(len(token)-1)]

    elif (token.startswith("।") or token.startswith("|") or token.startswith("?") \
                or token.startswith(",") or token.startswith("'") \
                or token.startswith("\"") or token.startswith("-") \
                or token.startswith(")") or token.startswith("(") \
                or token.startswith("\\") or token.startswith("}") \
                or token.startswith("{") or token.startswith(":") \
                or token.startswith(";") or token.startswith(".") \
                or token.startswith("?") or token.startswith("!")):
        cstr = token[1:(len(token))]

    return cstr;

def stem(s):
    s = tokenClean(s)
    if(isDictionaryWord(s) == 1):
        return s
    else:
        return stemmedToken(s)


# print(stem("পঢ়া"))
# print(stem("মন্দিৰ"))
# print(stem("খোৱাাতো"))
# print(stem("খোৱাাইছিলগৈ"))
# print(stem("পঢ়িলেগৈ"))
# print(stem("কৰক"))
# print(stem("আহিবাচোন"))
# print(stem("খোৱাানা"))
# print(stem("নাতিনীয়েক"))
# print(stem("চেৰেক"))
# print(stem("দুডাালমান"))
# print(stem("কৰকচোন"))
# print(stem("খোৱালৈ"))
# print(stem("মানুহকেইজনমান"))
# print(stem("ভাইয়েক"))
# print(stem("মানুহবোৰৰ"))
# print(stem("মানুহবোৰহে"))
# print(stem("মানুহজনহে"))
# print(stem("মানুহজনৰ"))
# print(stem("কৰিম"))
# print(stem("কৰিবাচোন"))
# print(stem("কৰিবিচোন"))
# print(stem("কৰিমগৈ"))
# print(stem("কৰোঁৱা"))
# print(stem("কৰোঁ"))
# print(stem("কৰিলো"))
# print(stem("কৰিম"))
# print(stem("কৰিছোঁ "))
# print(stem("কৰিছিলোঁ"))
# print(stem("কৰিমচোন"))
# print(stem("কৰিলি "))
# print(stem("কৰিবি"))
# print(stem("কৰিছ"))
# print(stem("কৰিছিলি"))
# print(stem("কৰাবা"))
# print(stem("কৰিবিচোন "))
# print(stem("কৰক "))
# print(stem("কৰিলে"))
# print(stem("কৰিব"))
# print(stem("কৰিছে "))
# print(stem("কৰিছিল"))
# print(stem("কৰোঁৱাওক"))
# print(stem("কৰিবচোন"))
# print(stem("কৰা"))
# print(stem("কৰিলা"))
# print(stem("কৰিবা"))
# print(stem("কৰিছা"))
# print(stem("কৰিছিলা"))
# print(stem("কৰোঁৱা"))
# print(stem("কৰিবাচোন"))


word_list = []
with open("/Users/partha/All/Python/ProjectMaterials/Learned material/Arts/Psychology.txt", encoding='utf-16') as file:
    for line in file:
        line = line.strip().replace("।", ".")
        word_list.append(line.strip())

# print(assamese_tokenizer(word_list))

f = open("/Users/partha/All/Python/ProjectMaterials/Stemming/assamese_stemmed_output.txt", "w", encoding="utf-16")
for w in assamese_tokenizer(word_list):
    # print(stem(w))
    f.write(stem(w)+'\n')
f.close()