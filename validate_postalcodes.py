import re
codes = raw_input()
print(bool(re.match(r'^[1-9][0-9]{5}$', codes) and len(re.findall(r'(\d)(?=\d\1)', codes)) < 2))
