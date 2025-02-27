import sys
def text_analyzer(text):
    """
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    """
    if not text:
        print("What is the text to analyze?")
        return
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            spaces += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punct += 1
    print("The text contains", len(text), "characters:")
    print("-", upper, "upper letters")
    print("-", lower, "lower letters")
    print("-", punct, "punctuation marks")
    print("-", spaces, "spaces")
    return

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        print("Error: invalid number of arguments.")