import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(text):
    if text in data:
        return data[text]
    else:
        word = text.lower()
        if word in data:
            return data[word]
        else:
            suggestions = get_close_matches(word, data.keys())
            if len(suggestions) > 0:
                closest_match = suggestions[0]
                return check_match(closest_match)
            else: return not_found_message(text)

def check_match(closest_match):
    yes_no = check_match_message(closest_match)
    if yes_no.lower() == "y":
        return data[closest_match]
    else: return not_found_message(word)

def check_match_message(word):
    return input("Did you mean '%s'? Enter Y for yes, N for no: " % word)

def not_found_message(word):
    return "'%s' is not found." % word


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
