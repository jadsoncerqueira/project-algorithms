def is_anagram(first_string: str, second_string: str):
    first_letters = list(first_string.lower())
    second_letters = list(second_string.lower())
    mer_sort(first_letters, 0, len(first_string))
    mer_sort(second_letters, 0, len(second_string))

    if len(first_string) == 0 or len(second_string) == 0:
        return ("".join(first_letters), "".join(second_letters), False)
    return (
        "".join(first_letters),
        "".join(second_letters),
        first_letters == second_letters,
    )


def mer_sort(letters, start, end):
    if (end - start) > 1:
        mid = (start + end) // 2
        mer_sort(letters, start, mid)
        mer_sort(letters, mid, end)
        mer(letters, start, mid, end)


def mer(letters, start, mid, end):
    letters_left = letters[start:mid]
    letters_right = letters[mid:end]
    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(letters_left):
            letters[general_index] = letters_right[right_index]
            right_index = right_index + 1
        elif right_index >= len(letters_right):
            letters[general_index] = letters_left[left_index]
            left_index = left_index + 1
        elif letters_left[left_index] < letters_right[right_index]:
            letters[general_index] = letters_left[left_index]
            left_index = left_index + 1
        else:
            letters[general_index] = letters_right[right_index]
            right_index = right_index + 1
