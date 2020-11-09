from sys import argv
with open(argv[1], newline='', encoding='utf-8-sig') as csvfile:
  for line in csvfile:
    print(line.strip('\n').split(','))