'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()