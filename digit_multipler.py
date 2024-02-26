num, op = 12345, 1
for n in [int(no) for no in str(num) if int(no) != 0 ]:
    op *= n
print(op)
