#!/usr/bin/python
#
# A simple python script to read and parse out the sbd message files sent by
# the Iridium phone in the Xeos beacon on the OOI 25 m test buoy.
#
# Created by Christopher Wingard, November 2009
import os
import sys
from datetime import datetime, date, time

# parse the command line inputs: python read_sbd.py outFile inFile
outFile = sys.argv[1]

# note, inFile can be "piped" in via standard in
if len(sys.argv) == 2:
    # assume input is from standard in
    inFile = ''
else:
    # otherwise use the named file
    inFile = sys.argv[2]

# read the mixed comma and space-delimited line, there is only one
if inFile == '':
    # read the data file from standard in
    strLine = sys.stdin.readline()
else:
    # otherwise read from a file
    fileIn = open(inFile, "r")
    strLine = fileIn.readline()
    fileIn.close()

# parse the input string
splOne = strLine.split(',')
splTwo = splOne[2].split(' ')

# assign the data to variables -- date and time
dateStr = splOne[0]  # the date and time string
utc = datetime.utcnow()  # what year is it today?
try:
    d = date(utc.year, int(dateStr[0:2]), int(dateStr[2:4]))
    t = time(int(dateStr[4:6]), int(dateStr[6:]))
    dt = datetime.combine(d, t)
except:
    sys.exit('Incorrect date format in SBD file, ignoring file %s' % inFile)

# assign the data to variables -- latitude and longitude
try:
    mode = splTwo[0]
    latitude = float(splTwo[1])
    longitude = float(splTwo[2])
    dCntr = int(splTwo[3])
    #tMode = int(splTwo[4])
    gpsLvl = int(splTwo[5])
    bVolt = float(splTwo[6])/100 
except:
    sys.exit('Incorrect position data in SBD file, ignoring file %s' % inFile)

# print the data to a file, appending as we go to create a single file.
fileOut = open(outFile, 'a')
fileOut.write('%sT%sZ\t%13.5f\t%14.5f\t%7d\t%5d\t%10.2f\n' % (dt.strftime('%Y-%m-%d'),
              dt.strftime('%H:%M'), latitude, longitude, dCntr, gpsLvl, bVolt))
fileOut.close()
