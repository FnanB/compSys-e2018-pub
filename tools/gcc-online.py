#!/usr/bin/env python3

import sys, re, os, mimetypes, argparse, requests

# -f <name of file> translates and assembles file
# -txl transform gcc output to x86prime
# -asm assemble x86prime into byte stream
# -list list (transformed and/or assembled) program
# -show show each simulation step (requires -run)
# -tracefile <name of file> create a trace file for later verification (requires -run)
# -run <name of function> starts simulation at indicated function (requires -asm)

parser = argparse.ArgumentParser(description='Compiles a C program into a gcc output x86_64.')

parser.add_argument('-o', dest='output',
                    help='Write output to this file')
parser.add_argument('file', metavar='C-file', 
                    help='translates and assembles file')

args = parser.parse_args()

extensions = args.file.split(".")
fileextension = extensions[-1]

if fileextension != "c":
  print("The input is expected to be a C program; fileextension 'c'.\n")
  exit()

if not os.path.isfile(args.file):
  print("Input file does not exist: "+args.file+"\n")
  exit()

file = open(args.file, 'r')
args.fileCont = file.read()
file.close()

# x86prime Online location
URL = "http://topps.diku.dk/compsys/gcc.php"
# defining a params dict for the parameters to be sent to the API
DATA = {'file':args.fileCont}
# sending get request and saving the response as response object
r = requests.post(url = URL, data = DATA)

URLDIR = "http://topps.diku.dk/compsys/gcc_runs/"
# extracting data in json format
runid = r.text

error = requests.get(url = URLDIR+runid+".error")

if error.text != "":
  print(error.text)
  exit()
else:
  assembler = requests.get(url = URLDIR+runid+".s")
  if args.output != None:
    file = open(args.output, 'w')
    args.fileCont = file.write(assembler.text)
    file.close()
  else:
    print(assembler.text)
