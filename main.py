def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    dict_list = dict_to_list(char_count)
    #sorted = sort_on(dict_list)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    print(char_count)
    print("----- TESTING STUFF -----")
    #test_items = char_count.items()
    print("::::: DICT TO LIST :::::")
    print(dict_list)
    print("")
    #print("::::: SORTED :::::")
    #print(sorted)
    #print("")


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
        if c.isalpha() != True:
            pass
        elif lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def dict_to_list(dictionary):
    list = []
    for ch, co in dictionary.items():
        entry = dict(char = ch, count = co)
        list.append(entry)
    return list


# vvv use this function to sort the list of dictionaries vvv
#def sort_on(dict):
#    return dict['count']

main()
