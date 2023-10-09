from io import StringIO


def generator(file_descriptor, list_search):
    words_set = set(map(lambda w: w.lower(), list_search))
    if isinstance(file_descriptor, str):
        with open(file_descriptor, "r", encoding="UTF-8") as file:
            yield from search_match_in_line(file, words_set)
    elif isinstance(file_descriptor, StringIO):
        file_descriptor.seek(0)
        yield from search_match_in_line(file_descriptor, words_set)
    else:
        raise TypeError("Expected a different type of variable")


def search_match_in_line(file, words_set):
    for line in file:
        line_set = set(line.strip().lower().split())
        if words_set & line_set:
            yield line
