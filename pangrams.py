# We promptly judged antique ivory buckles for the next prize : pangram
# We promptly judged antique ivory buckles for the prize : not pangram

# Enter the sentence
'pangram' if len(set(raw_input().lower().replace(" ", ""))) == 26 else 'not pangram'
