from __future__ import print_function # To work in python 2.x

number = [raw_input() for _ in range(int(raw_input()))]

def mobile(function):
    def phone(number):
        function("+1"+ "(" + num[-10:-7] + ")" + num[-7:-4]  + "-" + num[-4:] for num in number)
    return phone

@mobile
def sort_phone(number):
	print(*sorted(number), sep='\n')

sort_phone(number)
