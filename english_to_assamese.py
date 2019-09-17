def english_to_assamese(ch):
    if ch == "a":
        return "অ"
    elif ch == "aa":
        return "আ"
    elif ch == "_aa":
        return "া"
    elif ch == "i":
        return "ই"
    elif ch == "_i":
        return "ি"
    elif ch == "_ii":
        return "ী"
    elif ch == "u":
        return "উ"
    elif ch == "_u":
        return "ু"
    elif ch == "uu":
        return "ঊ"
    elif ch == "_uu":
        return "ূ"
    elif ch == "rri":
        return "ঋ"
    elif ch == "_rri":
        return "ৃ"
    elif ch == "e":
        return "এ"
    elif ch == "_e":
        return "ে"
    elif ch == "oi":
        return "ঐ"
    elif ch == "_oi":
        return "ৈ"
    elif ch == "o":
        return "ও"
    elif ch == "_o":
        return "ো"
    elif ch == "ou":
        return "ঔ"
    elif ch == "_ou":
        return "ৌ"
    elif ch == "k":
        return "ক"
    elif ch == "kh":
        return "খ"
    elif ch == "g":
        return "গ"
    elif ch == "gh":
        return "ঘ"
    elif ch == "Ng":
        return "ঙ"
    elif ch == "c":
        return "চ"
    elif ch == "ch":
        return "ছ"
    elif ch == "j":
        return "জ"
    elif ch == "jh":
        return "ঝ"
    elif ch == "nG":
        return "ঞ"
    elif ch == "T":
        return "ট"
    elif ch == "Th":
        return "ঠ"
    elif ch == "D":
        return "ড"
    elif ch == "Dh":
        return "ঢ"
    elif ch == "N":
        return "ণ"
    elif ch == "t":
        return "ত"
    elif ch == "th":
        return "থ"
    elif ch == "d":
        return "দ"
    elif ch == "dh":
        return "ধ"
    elif ch == "n":
        return "ন"
    elif ch == "p":
        return "প"
    elif ch == "ph" or ch == "f":
        return "ফ"
    elif ch == "b":
        return "ব"
    elif ch == "bh":
        return "ভ"
    elif ch == "m":
        return "ম"
    elif ch == "z":
        return "য"
    elif ch == "r":
        return "ৰ"
    elif ch == "l":
        return "ল"
    elif ch == "v" or ch == "w":
        return "ৱ"
    elif ch == "x":
        return "শ"
    elif ch == "S":
        return "ষ"
    elif ch == "s":
        return "স"
    elif ch == "h":
        return "হ"
    elif ch == "X":
        return "ক্ষ"
    elif ch == "R":
        return "ড়"
    elif ch == "Rh":
        return "ঢ়"
    elif ch == "y":
        return "য়"
    elif ch == "t~":
        return "ৎ"
    elif ch == "ng":
        return "ং"
    elif ch == "H":
        return "ঃ"
    elif ch == "^":
        return "ঁ"
    elif ch == ".":
        return "|"
    elif ch == "`":
        return "্"
    else:
        return ch
