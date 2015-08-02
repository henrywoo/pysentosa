from sentosa_ import tradingsystem
from ticktype import *
from config   import *
from nanomsg  import *
from websocket import create_connection
from multiprocessing import Process
from time import sleep
from signal import SIGINT
from os import kill

def run_daemon():
    ib = tradingsystem()
    print 'Mode:', yml_sentosa['global']['mode']
    ib.run()

class Merlion(object):
  def __init__(self, account=None):
    self.s1 = None
    self.account = yml_sentosa['global']['account']
    self.symbols = SYMBOLS
    self.trade_num = {}
    [self.trade_num.setdefault(i, 0) for i in self.symbols]
    self.p = None
    self.interest_list=[]

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
      while 1:
          try:
              url = 'ws://{}:16180/ws'.format(LOCALIP)
              self.ws = create_connection(url)
              return
          except:
              pass
              sleep(1)

  def get_mkdata(self):
    while self.s1:
      msg = self.s1.recv()
      if msg is not None and msg.index('|') > 0:
        v = msg.split('|')
        if len(v) == 3:
            if self.interest_list and v[0] in self.interest_list:
                print v[0], TTSTR[int(v[1])], v[2]
            if v[1] == str(ASK_PRICE) and float(v[2]) > 0:
                return v[0], ASK_PRICE, float(v[2])
            elif v[1] == str(BID_PRICE) and float(v[2]) > 0:
                return v[0], BID_PRICE, float(v[2])

  def track_msg(self, target):
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

  def run(self):
    self.p = Process(target=run_daemon)
    self.p.start()
    self.subscribe()
    self.connect_oms()
    return self
