pysentosa - Python API for sentosa trading system
============================================================================================

- pysentosa is the Python API for sentosa trading system written by Wu Fuheng

- WebSite: http://www.quant365.com (Quant365 - Trading with Science and Technology)

- OS: Linux Ubuntu 15.04 64bit

- Installation:

  ::

    sudo apt-get install -y python-pip libboost-all-dev libmysqlclient18 libyaml-cpp0.5
    sudo easy_install http://pypi.python.org/packages/2.7/p/pysentosa/pysentosa-0.1.18-py2.7.egg
    pip install pyyaml pymysql netifaces websocket-client nanomsg setproctitle psutil

- Launch your IB TWS.

- Run your strategy to trade

  Run demo:

  ::

    from pysentosa.demo import run_demo
    run_demo()

  Sample code:

  ::

    from pysentosa import Merlion, TT
    from ticktype import *

    m = Merlion()
    target = 'SPY'
    m.track_msg(target)
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
