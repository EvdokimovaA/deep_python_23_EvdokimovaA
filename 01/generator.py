import io


def search_matches(line, list_search):
    line_words = line.lower().split()
    for word in list_search:
        if word.strip(",.?:;!") in line_words:
            return True
    return False


def generator(file_descriptor, list_search):
    if isinstance(file_descriptor, (str, io.TextIOWrapper)):
        with open(file_descriptor, "r", encoding="UTF-8") as file:
            for line in file:
                if search_matches(line, list_search):
                    yield line
    else:
        raise TypeError("Expected a different type of variable")
