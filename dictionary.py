import json

data = json.load(open("data.json"))

def translate(text):
    word = text.lower()
    if word in data:
        return data[word]
    else:
        return "Word is not found."

word = input("Enter word: ")

print(translate(word))
