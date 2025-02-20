import requests
from spellchecker import SpellChecker
from colors_app import *

def check_spelling_grammar():
    text = input(f"\n{yellow}Enter text to check: ")
    spell = SpellChecker()
    words = text.split()
    misspelled = spell.unknown(words)

    if misspelled:
        print(f"\n🔍{lc} Spelling Suggestions:")
        for word in misspelled:
            correction = spell.correction(word)
            print(f"{green}- {word} → {correction if correction else 'No suggestion'}")
    else:
        print(f"✅{green} No spelling errors found!")
      #bad api ngl  should use ai instead -_-
      #to lazy to implement ai again -_-
    api_url = "https://api.languagetool.org/v2/check"
    params = {"text": text, "language": "en-US"}
    response = requests.post(api_url, data=params)

    if response.status_code == 200:
        result = response.json()
        if result["matches"]:
            print(f"\n📝{yellow} Grammar Suggestions:")
            for match in result["matches"]:
                print(f"- {match['message']}")
        else:
            print(f"✅{green} No grammar errors found!")
    else:
        print(f"⚠️{red} Error checking grammar!")



check_spelling_grammar()
