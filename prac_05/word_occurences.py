
letter_count = {}
phrase = input("Enter a string: ")
letters = phrase.split()
for letter in letters:
    freq = letter_count.get(letter, 0)
    letter_count[letter] = freq + 1

letters = list(letter_count.keys())
letters.sort()

length = max((len(letter) for letter in letters))
for letter in letters:
    print("{:{}} : {}".format(letter, length, letter_count[letter]))