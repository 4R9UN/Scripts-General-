import fileinput
import sys, os

fo = open("check.txt" ,"rb")

for bit in fo:
  #lines = bit.split()
  #print bit
  line = "\"" +"\\x" + bit.strip()  + ("\"")
  #print line 
  line = line.replace(' ', '\\x')
  print line
  f = open("final.txt" ,"ab")
  line = line + "\r\n"
  f.write(line)
  f.close()
