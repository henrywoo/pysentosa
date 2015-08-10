#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wu Fuheng(henry.woo@outlook.com)'
__version__= '0.1.18'

import os
import json

POSITION_STATUS = ["NOPOS",
        "OTL",
        "OTS",
        "DELIMITER",
        "LWaitC",
        "LWaitC2",
        "SWaitC",
        "SWaitC2",
        "NWaitL",
        "NWaitL2",
        "NWaitS",
        "NWaitS2"
]

def getTI0(mypath):
    if not os.path.exists(mypath):
        return None, None
    onlyfiles = [os.path.join(mypath,f) for f in os.listdir(mypath) if
                 os.path.isfile(os.path.join(mypath,f)) and f.endswith('json')]
    ti = None; dt= None
    tmp = None
    pat = None
    for f in onlyfiles:
        dt = f.split(os.sep)[-1].split('.')[0]
        if f.endswith('vola.json'):
            pass
        else:
            if tmp is None or tmp < dt:
                tmp = dt
                pat = f

    if os.path.exists(pat):
        j = json.load(open(pat))
        ti = j['_tinfo']
    return ti, tmp


def getTI(sym):
    from config import TRADEINFODIR
    mypath = TRADEINFODIR + os.sep + sym
    return getTI0(mypath)

def getTI2(sym, dt):
    from config import TRADEINFODIR
    mypath = TRADEINFODIR + os.sep + sym + os.sep + dt + '.json'
    j = json.load(open(mypath))
    ti = j['_tinfo']
    return ti, dt


if __name__ == "__main__":
    from pprint import pprint
    ti, dt = getTI('TAOM')
    pprint(ti)