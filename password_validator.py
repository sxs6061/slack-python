import re
data ='QwErTy911poqqqq'
print  bool(re.findall(r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}', data))
