#!/usr/bin/env python3

import sys, re, os, mimetypes, argparse, requests

# -f <name of file> translates and assembles file
# -txl transform gcc output to x86prime
# -asm assemble x86prime into byte stream
# -list list (transformed and/or assembled) program
# -show show each simulation step (requires -run)
# -tracefile <name of file> create a trace file for later verification (requires -run)
# -run <name of function> starts simulation at indicated function (requires -asm)

parser = argparse.ArgumentParser(description='Transform gcc output to x86\', assemble and simulate.')
parser.add_argument('-f', dest='file',
                    help='translates and assembles file')
parser.add_argument('-asm', dest='asm', action='store_const',
                    const=True, default=False,
                    help='assemble x86prime into byte stream')
parser.add_argument('-txl', dest='txl', action='store_const',
                    const=True, default=False,
                    help='transform gcc output to x86prime')
parser.add_argument('-list', dest='list', action='store_const',
                    const=True, default=False,
                    help='list (transformed and/or assembled) program')
parser.add_argument('-show', dest='show', action='store_const',
                    const=True, default=False,
                    help='show each simulation step (requires -run)')
parser.add_argument('-tracefile', dest='tracefile',
                    help='create a trace file for later verification (requires -run)')
parser.add_argument('-run', dest='procedure',
                    help='starts simulation at indicated procedure (requires -asm)')

args = parser.parse_args()

if args.file==None :
  print("Program needs an input file.\n")
  parser.print_help()
  exit()

extensions = args.file.split(".")
fileextension = extensions[-1]

if fileextension != "s":
  print("The input is expected to be a assembler program; fileextension 's'.\n")
  exit()

if args.file==None :
  print("Program needs an input file.\n")
  parser.print_help()
  exit()

if not os.path.isfile(args.file):
  print("Input file does not exist: "+args.file+"\n")
  exit()

file = open(args.file, 'r')
args.fileCont = file.read()
file.close()

# x86prime Online location
URL = "http://topps.diku.dk/compsys/x86prime.php"
# defining a params dict for the parameters to be sent to the API
DATA = {'file':args.fileCont, 'txl':args.txl, 'asm':args.asm, 'list':args.list, 'show':args.show, 'tracefile':args.tracefile, 'procedure':args.procedure}
# sending get request and saving the response as response object
r = requests.post(url = URL, data = DATA)

URLDIR = "http://topps.diku.dk/compsys/x86prime_runs/"
# extracting data in json format
runid = r.text

error = requests.get(url = URLDIR+runid+".error")
output = requests.get(url = URLDIR+runid+".out")

if error.text != "":
  print(error.text)
  exit()
else:
  output = requests.get(url = URLDIR+runid+".out")
  print(output.text)

if args.tracefile != None:
  trace = requests.get(url = URLDIR+runid+".trace")
  file = open(args.tracefile, 'w')
  args.fileCont = file.write(trace.text)
  file.close()

