import re
text = ("bright aright", "ok")
print(','.join(i.replace('right', 'left') for i in text))
