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
            closest_match = suggestions[0]
            yes_no = input("Did you mean '%s'? Enter Y for yes, N for no." % closest_match)
            if yes_no.lower() == "y":
                return data[closest_match]
            else: return not_found(word)
        else: return not_found(word)

def not_found(lookup):
    return "'%s' is not found." % lookup

word = input("Enter word: ")

print(translate(word))
