import sys
import os

RedirectIOToFile = False

if RedirectIOToFile:
  gCwd = os.getcwd()
  gScriptDir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(gScriptDir)
  sys.stdin = open("./014_Tuples_Inputs.txt")

def CloseIO()->None:
  if RedirectIOToFile:
    sys.stdin.close()
    os.chdir(gCwd)

if __name__ == '__main__':
  n = input()
  t = tuple(map(int, input().split()))      # read values as int
  print(f"{hash(t)}")                       

  CloseIO()