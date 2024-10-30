import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead "%get_close_matches(word,data.keys()))
        decide = input("Press Y or N for yes or no → ")
        if decide.capitalize() == "Y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide.capitalize() == "N" :
            return "You have entered a wrong key "
        else:
            return "You have entered wrong input please just enter [Y-N]"
    else:
        return "You have entered a wrong key or perhaps it isn't available in our dictionary "
        

while True:
    word = input("Enter the word to search meaning: ")
    output = translate(word)

    if type(output) == list:
        i = 1
        for item in output:
            print(i,"-",item,"\n")
            i = i+1
    else:
        print(output)