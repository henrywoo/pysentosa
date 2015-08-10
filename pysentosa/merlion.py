#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wu Fuheng(henry.woo@outlook.com)'
__version__= '0.1.18'

from sentosa_ import tradingsystem
from ticktype import *
from config   import *
from nanomsg  import *
from websocket import create_connection
from multiprocessing import Process
from time import sleep
from signal import SIGINT
from os import kill
from setproctitle import setproctitle

def run_daemon():
    setproctitle('sentosa')
    ib = tradingsystem()
    print "Running sentosa with python"
    print 'Mode:', yml_sentosa['global']['mode']
    ib.run()

def isSentosaRunning():
    import psutil
    for proc in psutil.process_iter():
        pname = proc.name()
        if pname=="sentosa" or pname=='SENTOSA':
            return True
    return False

class Merlion(object):
  def __init__(self, account=None):
    self.s1 = None
    self.account = yml_sentosa['global']['account']
    if self.account == 'DU198456':
        print "ERROR: You haven't set your IB account yet.\nYou just need to open " \
              "~/.sentosa/sentosa.yml, find account under global section, " \
              "and replace the demo account with your own IB account."
        import sys
        sys.exit(-1)
    self.symbols = SYMBOLS
    self.trade_num = {}
    [self.trade_num.setdefault(i, 0) for i in self.symbols]
    self.p = None
    self.interest_list=[]

    if not isSentosaRunning():
        self.run_sentosa()

    self.subscribe()
    self.connect_oms()

  def rerun(self):
    if self.p:
      kill(self.p.pid, SIGINT)
      sleep(3)
      self.run()

  def subscribe(self):
    self.s1 = Socket(SUB)
    url = 'tcp://127.0.0.1:{}'.format(yml_sentosa['global']['MKD_TO_ALGO_PORT'])
    self.s1.connect(url)
    self.s1.set_string_option(SUB, SUB_SUBSCRIBE, '')

  def connect_oms(self):
      count = 0
      while 1:
          try:
              url = 'ws://{}:16180/ws'.format(LOCALIP)
              self.ws = create_connection(url)
              return
          except:
              sleep(1)
              count += 1
              if (count % 11 == 0):
                  print 'ERROR: Cannot connect to sentosa server'

  def get_mkdata(self):
    while self.s1:
      msg = self.s1.recv()
      if msg is not None and msg.index('|') > 0:
        if msg[-1] == '\0':
            msg = msg[:-1]
        v = msg.split('|')
        if len(v) == 3:
            if self.interest_list and v[0] in self.interest_list:
                print v[0], TTSTR[int(v[1])], v[2]
            if v[1] == str(ASK_PRICE) and float(v[2]) > 0:
                return v[0], ASK_PRICE, float(v[2])
            elif v[1] == str(BID_PRICE) and float(v[2]) > 0:
                return v[0], BID_PRICE, float(v[2])

  def track_symbol(self, target):
    if isinstance(target, list):
        map(self.interest_list.append, target)
    elif isinstance(target, str):
        self.interest_list.append(target)

  def get_balance(self):
    pass

  def get_uPNL(self):
    pass

  def get_aPNL(self):
    pass

  def buy(self, ticker, share):
    msg='m|{}|{}'.format(ticker,share)
    self.ws.send(msg)

  def sell(self, ticker, share):
    msg='m|{}|{}'.format(ticker,-share)
    self.ws.send(msg)

  def run_sentosa(self):
    self.p = Process(target=run_daemon)
    self.p.start()
    return self

if __name__ == '__main__':
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
            bounds[symbol][1] += 10
