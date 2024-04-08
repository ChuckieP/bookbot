def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    char_count = count_chars(text)
    print(char_count)


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


main()
