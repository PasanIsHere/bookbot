def countWords(text):
    return len(text.split())

def countChars(text):
    char_count = {} # Key = character , Value = Number of times it appears
    for c in text.lower():
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def printReport(book,text):
    print("--- Begin report of "+ book +" ---")
    word_count = countWords(text)
    char_count = countChars(text)
    
    print(f"{word_count} words found in the document\n\n")
    for k,v in char_count.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End Report ---")
    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    printReport("books/frankenstein.txt", file_contents)


main()
                            
