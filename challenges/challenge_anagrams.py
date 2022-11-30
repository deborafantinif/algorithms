def sorted_word(word):
    n = len(word)

    for index in range(n - 1):
        min_element_index = index

        for search_index in range(index + 1, n):
            if word[search_index] < word[min_element_index]:
                min_element_index = search_index

        current_element = word[index]
        word[index] = word[min_element_index]
        word[min_element_index] = current_element

    return word


def is_anagram(first_string, second_string):
    first_formated = sorted_word(first_string.lower())
    second_formated = sorted_word(second_string.lower())

    if len(first_string) != len(second_string):
        return (first_formated, second_formated, False)
    else:
        return (first_formated, second_formated, True)

