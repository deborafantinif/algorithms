def is_palindrome_iterative(word):
    if word == '':
        return False

    n = len(word) - 1
    initial = 0

    while n > initial:
        if word[initial] != word[n]:
            return False
        n -= 1
        initial += 1

    return True
