
def build_shift_table(real_substring):

    table = {}
    length = len(real_substring)

    for index, char in enumerate(real_substring[:-1]):
        table[char] = length - index - 1

    table.setdefault(real_substring[-1], length)
    return table


def bm_search(text, real_substring):

    shift_table = build_shift_table(real_substring)
    i = 0 

    while i <= len(text) - len(real_substring):
        j = len(real_substring) - 1 

        while j >= 0 and text[i + j] == real_substring[j]:
            j -= 1 

        if j < 0:
            return i 

        i += shift_table.get(text[i + len(real_substring) - 1], len(real_substring))

    return -1

