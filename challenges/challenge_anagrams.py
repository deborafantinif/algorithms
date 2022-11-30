def sorted_word(word, start, end):
    if start < end:
        p = partition(word, start, end) 
        sorted_word(word, start, p - 1)
        sorted_word(word, p + 1, end)

def partition(word, start, end):
    pivot = word[end]
    delimiter = start - 1

    for index in range(start, end):
        if word[index] <= pivot:
            delimiter = delimiter + 1
            word[index], word[delimiter] = word[delimiter], word[index]

    word[delimiter + 1], word[end] = word[end], word[delimiter + 1]

    return delimiter + 1

def is_anagram(first_string, second_string):
    first_formated = list(first_string.lower())
    second_formated = list(second_string.lower())
    sorted_word(first_formated, 0, (len(first_formated) - 1))
    sorted_word(second_formated, 0, (len(second_formated) - 1))
    first_formated = ','.join(first_formated).replace(',','')
    second_formated = ','.join(second_formated).replace(',','')

    if first_formated != second_formated or first_string == '' or second_formated == '':
        return (first_formated, second_formated, False)
    else:
        return (first_formated, second_formated, True)

