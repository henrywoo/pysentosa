pysentosa - Python API for sentosa trading system
============================================================================================

- pysentosa is the Python API for sentosa trading system written by Wu Fuheng

- WebSite: http://www.quant365.com (Quant365 - Trading with Science and Technology)

- OS: Linux Ubuntu 15.04 64bit

- Installation:

  ::

    sudo apt-get install -y python-pip libboost-all-dev libyaml-cpp0.5
    sudo easy_install http://pypi.python.org/packages/2.7/p/pysentosa/pysentosa-0.1.25-py2.7.egg
    sudo pip install pyyaml netifaces websocket-client nanomsg setproctitle psutil

- Launch your IB TWS.

- Run your strategy to trade

  Run demo:

  ::

    from pysentosa.demo import run_demo
    run_demo()

  Sample code:

  ::

    from pysentosa import Merlion
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
              bounds[symbol][1] += 20


.. image:: https://d2weczhvl823v0.cloudfront.net/henrywoo/pysentosa/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

