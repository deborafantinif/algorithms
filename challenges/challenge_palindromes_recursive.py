def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    if low_index == high_index:
        return True
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    next_low_index = low_index + 1
    next_high_index = high_index + 1
    return is_palindrome_recursive(word, next_low_index, next_high_index)

