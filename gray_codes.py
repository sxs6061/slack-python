# Given a number of n, generate a possible gray code for it.
# Eg. for n = 2, one gray code would be [00, 01, 10, 11]

# Using list comprehension:
def gray_code(n):
    return  ([ "{0:0{1}b}".format(i,n) for i in xrange(2**n) ])

print " ".join(gray_code(2)),


# Using Bitwise operarions:
# def main():
#     n=int(raw_input())
#     for i in range(0, 1<<n):
#         gray=i^(i>>1)
#         print "{0:0{1}b}".format(gray,n),

# main()
