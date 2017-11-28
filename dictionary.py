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
        closest_match = suggestions[0]
        if len(suggestions) > 0:
            yes_no = input("Did you mean '%s'? Enter Y for yes, N for no." % closest_match)
            if yes_no.lower() == "y":
                return closest_match

        else: "'%s' is not found." % word

word = input("Enter word: ")

print(translate(word))
