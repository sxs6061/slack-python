import re
def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    length = 0
    match = ''
    for y in range(len(line)):
        for x in range(1,len(line)+1):
            substring = line[y:x]
            if len(list(re.finditer(re.escape(substring),line))) > 1  and len(substring) > length:
                match = substring
                length = len(substring)
    return len(match)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
