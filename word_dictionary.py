from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break

    meanings = dictionary.meaning(word)
    if meanings:
        for part_of_speech, definitions in meanings.items():
            print(f"{part_of_speech.capitalize()}:")
            for index, definition in enumerate(definitions, start=1):
                print(f"{index}. {definition}")
    else:
        print("Word not found in the dictionary.")
