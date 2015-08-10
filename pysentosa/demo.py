#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wu Fuheng(henry.woo@outlook.com)'
__version__= '0.1.18'

def run_demo():
  s='''from pysentosa import Merlion
from ticktype import *
m = Merlion()
target = 'SPY'
m.track_symbol([target, 'BITA', 'NTES', 'GOOG'])
bounds = {target: [200, 250]}
while True:
  symbol, ticktype, value = m.get_mkdata()
  if symbol == target:
    if ticktype == ASK_PRICE and value < bounds[symbol][0]:
        m.buy(symbol, 100)
        bounds[symbol][0] -= 10
    elif ticktype == BID_PRICE and value > bounds[symbol][1]:
        m.sell(symbol, 100)
        bounds[symbol][1] += 10'''
  print '*'*80
  print s
  print '*'*80
  exec(s)

if __name__ == '__main__':
  run_demo()
