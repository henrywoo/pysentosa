#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wu Fuheng(henry.woo@outlook.com)'
__version__= '0.1.28'

def run_demo():
  s='''from pysentosa import Merlion
from ticktype import *

m = Merlion()
target = 'SPY'
m.track_symbol([target, 'BITA'])
bounds = {target: [220, 250]}
while True:
  symbol, ticktype, value = m.get_mkdata()
  if symbol == target:
    if ticktype == ASK_PRICE and value < bounds[symbol][0]:
        oid = m.buy(symbol, 5)
        while True:
            ord_st = m.get_order_status(oid)
            print ORDSTATUS[ord_st]
            if ord_st == FILLED:
                bounds[symbol][0] -= 20
                break
            sleep(2)
    elif ticktype == BID_PRICE and value > bounds[symbol][1]:
        oid = m.sell(symbol, 100)
        bounds[symbol][1] += 20'''
  print '*'*80
  print s
  print '*'*80
  exec(s)

if __name__ == '__main__':
  run_demo()
