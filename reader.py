def string_generator():
    with open("sentences.txt","r") as f:
        return iter([l.strip() for l in f.readlines()])
