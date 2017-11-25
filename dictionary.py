import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(text):
    word = text.lower()
    if word in data:
        return data[word]
    else:
        suggestions = get_close_matches(word, data.keys())
        if len(suggestions) > 0:
            return "Did you mean '%s'?" % suggestions[0]
        else: "Word is not found."

word = input("Enter word: ")

print(translate(word))
