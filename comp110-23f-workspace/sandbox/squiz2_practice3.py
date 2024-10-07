"""Short Words"""

def short_words(input_list: list[str]) -> list[str]:
    """Returns a new list of strings containing words shorter than 5 characters"""
    short_list: list[str] = []
    for word in input_list:
        if len(word) < 5:
            short_list.append(word)
        else:
            print(f"{word} is too long!")
    return short_list

print(short_words(["a" ,"aa", "aaa", "aaaa", "aaaaa"]))