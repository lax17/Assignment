
# word count
with open("testfile.txt","r") as f:
    word_count = 0
    for line in f:
        if "," in line:
            line = line.replace(","," ")
        words= line.split()
        word_count += len(words)

print("Total Number of Words " + str(word_count))