with open("sentences.txt","r") as f:
    current_strings = iter([l.strip() for l in f.readlines()])
