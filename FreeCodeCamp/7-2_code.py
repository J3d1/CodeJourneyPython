# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open("/home/derek/CodeJourney/CodeJourneyPython/FreeCodeCamp/mbox-short.txt")
averg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    atpos = line.find(' ')
    value = float(line[atpos+1:])
    count = count + 1 
    averg = averg + value
print("Average spam confidence:", averg/count)