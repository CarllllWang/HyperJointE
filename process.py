tuples = []

with open("./data/WikiPeople-4/test.txt") as f:
    for line in f.readlines():
        line = line.strip().split()
        tuples.append("\t".join(line))
    f.close()

with open("./data/WikiPeople-4/test.txt", "w") as f:
    for tuple in tuples:
        f.write(tuple + "\n")

    f.close()