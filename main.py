def run(mode):
  with open("upper_test1.txt", mode) as output:
    lines = ['abc', 'def', 'ghi']
    output.writelines(lines)

if __name__ == "__main__":
  run('w')