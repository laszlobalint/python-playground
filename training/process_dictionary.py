import pickle


def load_files(path="dictionary_content"):
    eng_hun_dictionary = {}
    try:
        i = 0
        while True:
            filename = "{}/dict{}.txt".format(path, i)
            i += 1
            with open(filename, "r", encoding="windows-1250") as file:
                for row in file:
                    key, value = row.strip().replace(";", "; ").split("#")
                    eng_hun_dictionary[key] = value
    except Exception:
        print("Files read!")
    return eng_hun_dictionary


try:
    dictionary = pickle.load(open("dictionary.dat", "rb"))
except Exception as exception:
    dictionary = load_files()
    pickle.dump(dictionary, open("dictionary.dat", "wb"))

english_word = input("Please, give an english expression (or nothing to exit): ")
while english_word:
    print("{} = {}".format(english_word,
                           dictionary.get(english_word.strip(), "Expression does not exist in the dictionary!")))
    english_word = input("Please, give an english expression (or nothing to exit): ")
