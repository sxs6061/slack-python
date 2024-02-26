# Sample Input
# 3
# DEXTER <dexter@hotmail.com>
# SOM <som@gmail.com>
# VIRUS <virus!@variable.:p>

# Sample Output
# DEXTER <dexter@hotmail.com>
# SOM <som@gmail.com>
from email.utils import parseaddr
import re

pattern = r"^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$"

# Enter number followed by name and email (name <user@email.com>)
data = [ raw_input() for count in range(int(raw_input())) ]
print('\n'.join([ email for email in data if re.match(pattern, parseaddr(email)[1]) ]))
