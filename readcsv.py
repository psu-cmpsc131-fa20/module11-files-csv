from sys import argv
import csv
with open(argv[1], newline='', encoding='utf-8-sig') as input:
  csvfile = csv.reader(input)
  for row in csvfile:
    print(row)