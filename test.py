import os
import numpy
import csv
import sys

from datetime import date

FILE_NAME = "temp.txt"
DATA_FILE_NAME = "data.csv"

def photonesAndTimeStats(i):
  print("\n->Getting time and photones from program")
  photonesAverage = 0
  timeAverage = 0
  photonesLectures = []
  timeLectures = []
  for x in range(i):
    os.system(f"./tiny_mc > {FILE_NAME}")
    file = open(FILE_NAME)
    content = file.readlines()
    time = float(content[7].split()[1])
    photones = float(content[8].split()[1])
    photonesLectures.append(photones)
    timeLectures.append(time)
  print("-->Done")
  return (photonesLectures,timeLectures)

def perfStats(i):
  print("\n->Getting stats from perf stats")
  os.system(f"perf  stat -x ',' -o {FILE_NAME} -r {i} ./tiny_mc > /dev/null")
  file = open(FILE_NAME)
  content = file.readlines()
  instructionsPerSecond = content[9].split(",")[6]
  print("-->Done")
  return instructionsPerSecond

def perfStatsLinares(i):
  print("\n->Getting stats from perf stats")
  os.system(f"sudo perf stat -o {FILE_NAME} -r {i} ./tiny_mc > /dev/null")
  file = open(FILE_NAME)
  content = file.readlines()
  instructionsPerSecond = content[12].split("#")[1].split(" ")[4].replace(",",".")
  return instructionsPerSecond

def writeInfo(a,b):
  print(f"\n->Writting info in {DATA_FILE_NAME}")
  existFile = os.path.isfile("./"+DATA_FILE_NAME)
  fileFlags = "a" if existFile else "w"
  with open(DATA_FILE_NAME, fileFlags, newline="" ) as file:
    writer = csv.writer(file)
    headers = ["type","photones","time","instuctions per cycle","description","date"]
    if(not existFile):
      writer.writerow(headers)
    a.append(date.today())
    b.append(date.today())
    writer.writerow(a)
    writer.writerow(b)
  print("-->DONE")

def main():
  repeat = 15
  print(f"Starting test with repeat={repeat}")
  (a,b) = photonesAndTimeStats(repeat)
  c = perfStats(repeat)
  description = "NONE"
  if(len(sys.argv) >= 2):
    description = str(sys.argv[1])
    print(f"\nUsing {description} as descripcion for the test")
  else:
    print("\nDescription was not provided, using NONE") 
  average =["Average",numpy.average(a),numpy.average(b),c,description]
  dev =["Deviation",numpy.std(a),numpy.std(b),0,description]
  writeInfo(average,dev)
  print("\nTest finished")

if __name__ == "__main__":
  main()

