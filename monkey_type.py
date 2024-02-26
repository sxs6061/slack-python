text, words =("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
print(sum(w in text.lower() for w in words))
