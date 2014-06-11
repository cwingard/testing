#!/usr/bin/python
"""
first pass at reading and parsing the acs dev file to extract required
calibration values

C. Wingard 2014-05-02
"""

import numpy as np
import string
import re

# read the ac-s device file
with open('OPTAA_ACS135_Calibration_2013-04-29.dev', 'r') as dev:
    data = dev.readlines()

# parse data for the number of temperature bins and the temperature values
nBins = np.array(data[8].strip().split()[0]).astype(np.int)
tbins = np.array(data[9].strip().split())
tbins = tbins[:-3].astype(np.float)

# convert the rest of the data for the wavelengths, offsets and temperature
# correction arrays
nWlngth = np.array(data[7].strip().split()[0]).astype(np.int)
arr = np.zeros([nWlngth, (nBins*2)+5]).astype(np.float)
for iRow in range(10, len(data)-1):
    tmp = data[iRow].strip().split()[:-12]
    tmp[0] = tmp[0].translate(None, string.letters)
    tmp[1] = tmp[1].translate(None, string.letters)
    tmp[2] = 0
    arr[iRow-10, :] = np.array(tmp).astype(np.float)

cwl = arr[:, 0]
awl = arr[:, 1]
coff = arr[:, 3]
aoff = arr[:, 4]
tc_arr = arr[:, 5:5+nBins]
ta_arr = arr[:, 5+nBins:]

# now pretty-print (sort of)
tbins = np.array_str(tbins, max_line_width=10000, precision=6)
tbins = re.sub('\s{1,10}', ',', tbins)

cwl = np.array_str(cwl, max_line_width=10000, precision=1)
cwl = re.sub('\s{1,10}', ',', cwl)
awl = np.array_str(awl, max_line_width=10000, precision=1)
awl = re.sub('\s{1,10}', ',', awl)
coff = np.array_str(coff, max_line_width=10000, precision=6)
coff = re.sub('\s{1,10}', ',', coff)
aoff = np.array_str(aoff, max_line_width=10000, precision=6)
aoff = re.sub('\s{1,10}', ',', aoff)

tc_arr = np.array_str(tc_arr, max_line_width=10000, precision=6)
tc_arr = re.sub('\n\s', ',', tc_arr)
tc_arr = re.sub('\s{1,10}', ',', tc_arr)

ta_arr = np.array_str(ta_arr, max_line_width=10000, precision=6)
ta_arr = re.sub('\n\s', ',', ta_arr)
ta_arr = re.sub('\s{1,10}', ',', ta_arr)

