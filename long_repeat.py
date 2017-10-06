def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    repeat = 0
    while any(line):
        line = [ line[i] and line[i] == line[i+1] for i in range(len(line)-1) ]
        repeat += 1
    return repeat

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
