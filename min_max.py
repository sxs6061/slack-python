def checkio(*args):
    print(max(args)-min(args) if len(args)>0 else 0)

if __name__ == '__main__':
    checkio(1, 2, 3)
