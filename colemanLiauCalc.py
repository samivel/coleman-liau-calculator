from cs50 import get_string

# Gets input
story = get_string("Text: ")

# Finds number of letters in input
letters = 0
for i in story:
    if i.isalpha():
        letters += 1
# print("{} Letters".format(letters))

# Finds number of words in input
words = len(story.split())
# print("{} Words".format(words))

# Finds number of sentences in input
sentences = 0
for i in range(0, len(story)):
    if story[i] in ('!', ".", "?"):
        sentences += 1
# print("{} Sentences".format(sentences))

# Finds grade number
l100 = letters / words * 100
s100 = sentences / words * 100
grade = round((0.0588 * l100 - 0.296 * s100 - 15.8))

# Prints results
if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade {}".format(grade))
