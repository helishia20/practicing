
string = 'Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven'
words = string.split(" ")
print(words)

number = {"Dash": '  ', "Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4,
          "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9}

for w in words:
    if w in number:
        print(number[w],end="")
    else:
        print(w[0],end="")
