# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from click import open_file


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("C:/Users/NCC/Desktop/Web Dev/Zuri Python/Reading-Text-Files/story.txt", "r") as openfile:
        read_file_content = openfile.read()
    return read_file_content
        # print(read_file_content)
 


def count_words():
    text = read_file_content("C:/Users/NCC/Desktop/Web Dev/Zuri Python/Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    
    split_text = text.split()
    # print(split_text)
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
             count[i] = 1
    return count
print(count_words())
