from sys import argv
import csv
with open(argv[1], newline='', encoding='utf-8-sig') as inputfile:
  csvfile = csv.reader(inputfile)
  for row in csvfile:
    print(row)