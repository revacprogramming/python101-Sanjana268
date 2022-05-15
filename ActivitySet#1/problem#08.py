# Files

#filename = "dataset/mbox-short.txt"
def find_avg(fc,ft):
    fname = input("Enter file name: ")
    fh = open(fname)
    fc = 0
    ft = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        x=line.find("0")
        y= float(line[x:])
        fc = fc + 1
        ft = ft + y

    average = ft/fc
    print("Average spam confidence:",average)

count=0
total=0
average=find_avg(count,total)
