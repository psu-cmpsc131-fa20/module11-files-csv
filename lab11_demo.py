from sys import argv
import csv
def run():
  if len(argv) < 3:
    print(f"Usage: python3 {argv[0]} originalfile newfile")
    return
  with open(argv[1], newline='') as original:
    csvOriginal = csv.DictReader(original, dialect='excel')
    print(csvOriginal.fieldnames)
    with open(argv[2], 'w', newline='') as newFile:
      csvNew = csv.DictWriter(newFile, csvOriginal.fieldnames, dialect='excel-tab')
      csvNew.writeheader()
      rows = []
      for row in csvOriginal:
        rows.append(row)
      sortedrows = sorted(rows, key = lambda row:row['Last'], reverse=True)
      csvNew.writerows(sortedrows)
      

if __name__ == "__main__":
  run()