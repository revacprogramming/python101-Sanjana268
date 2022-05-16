# Tuples

#filename = "dataset/mbox-short.txt"
name = input("Enter file:")
handle = open(name)
hours = dict()
for line in handle:
    if line.startswith("From "):
        L = line.split()
        time = L[len(L)-2].split(":")
        hours[time[0]] = hours.get(time[0], 0) + 1
res = sorted(list(hours.items()))
for i,j in res:
    print(i,j)

