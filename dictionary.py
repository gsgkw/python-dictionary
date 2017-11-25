import json

data = json.load(open("data.json"))

def translate(text):
    return data[text]

word = input("Enter word")

print(translate(word))
