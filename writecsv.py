from sys import argv
import csv
with open(argv[1], newline='', encoding='utf-8-sig') as inputfile:
  with open(argv[2], "w", newline='') as outputfile:
    csvfile = csv.DictReader(inputfile)
    csvoutput = csv.DictWriter(outputfile, csvfile.fieldnames)
    csvoutput.writeheader()
    t = []
    for row in csvfile:
      t.append(row)
    t.reverse()
    csvoutput.writerows(t)

