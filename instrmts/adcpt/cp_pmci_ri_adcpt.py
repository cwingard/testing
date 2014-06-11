#!/usr/bin/env python
#
# cp_pmci_ri_adcpt.py
#
# Tests application of DPAs to ADCPT data, for CP02PMCI, downloaded from the
# OOINet ERDDAP dataset. Purpose is to compare results from direction
# computation of data products using DPAs with outputs available in OOINet.
#
# Created by C. Wingard, June 2014.

# import main python modules
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# load the OOI Tool Kit
from ooitk.session import ERDDAPSession

def convert_time(t,p):
    dtg = datetime.utcfromtimestamp(t)
    return dtg.isoformat()

# set the dataset url and open session to download data
erddap = 'http://erddap.b.oceanobservatories.org:8080/erddap/tabledap/data7351f78f313c4010be85992fc761ac39.html'
session = ERDDAPSession(erddap)
session.open()

