import collections


def find_duplicate(nums):
    if nums == []:
        return False

    number_checked = collections.Counter(nums).most_common()
    if number_checked[0][1] == 1 or number_checked[0][0] <= 0:
        return False
    else:
        return number_checked[0][0]
