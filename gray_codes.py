# Given a number of buts n, generate a possible gray codefor it.
# Eg. for n = 2, once gray code would be  [00, 01, 10, 11]
def main():
    n=int(raw_input())
    for i in range(0, 1<<n): # bitwise left same as multiplying 1 by 2**n. 
        gray=i^(i>>1) # bitwise right same as //'ing i by 2**1
        print "{0:0{1}b}".format(gray,n), # formatting in binary and padding 0s 

main()