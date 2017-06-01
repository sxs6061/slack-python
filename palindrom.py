# Nurses run : Palindrom
s = raw_input().lower().replace(" ", "")
print 'Palindrom' if(s[::-1] == s) else 'Not palindrom'
