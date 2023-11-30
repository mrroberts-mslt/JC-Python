word = input("Please enter a word: ")
first = word[0]
rest = word[1:]
#wordLen = len(word)
print(first)
print(rest)

if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    first = "piggy"
    pigLatin = first + rest
    
else:
    first = "umchy"
    pigLatin = first + rest
print(pigLatin.capitalize())
