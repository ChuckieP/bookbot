def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    print(char_count)
    print("----- TESTING STUFF -----")
    #test_items = char_count.items()
    test_list = dict_to_list(char_count)
    print("::::: ITEMS :::::")
    print(test_list)
    print("")



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(str_input):
    words = str_input.split()
    return len(words)


def count_chars(str_input):
    chars = {}
    for c in str_input:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def dict_to_list(dict):
    list = []
    for i in dict:
        list.append(i)
    return list


# vvv use this function to sort the list of dictionaries vvv
#def sort_on(dict):
#    pass

main()
