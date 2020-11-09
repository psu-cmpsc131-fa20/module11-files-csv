from sys import argv
def run_iteration():
  print(f"Reading {argv[2]} using iteration.")
  with open(argv[2]) as file:
    for line in file:
      print(line, end='')

def run_read():
  print(f"Reading {argv[2]} using read().")
  with open(argv[2]) as file:
    print(file.read(), end='')

def run_readlines():
  print(f"Reading {argv[2]} using readlines().")
  with open(argv[2]) as file:
    lines = file.readlines()
    print(lines)

def run_readline():
  print(f"Reading {argv[2]} using readline().")
  with open(argv[2]) as file:
    line = file.readline()
    while line != '':
      print(line, end='')
      line = file.readline()

if __name__ == "__main__":
  if len(argv) < 3:
    print(f"Usage: python3 {argv[0]} options(iteration/read/readlines/readline) filename")
  elif argv[1] == 'iteration':
    run_iteration()
  elif argv[1] == 'read':
    run_read()
  elif argv[1] == 'readlines':
    run_readlines()
  elif argv[1] == 'readline':
    run_readline()
                    