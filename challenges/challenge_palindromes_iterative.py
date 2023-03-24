def is_palindrome_iterative(word):
    if word == "":
        return False

    l_index = 0
    h_index = len(word) - 1

    while l_index < h_index:
        if word[l_index] == word[h_index]:
            l_index += 1
            h_index -= 1
        else:
            return False
    return True
