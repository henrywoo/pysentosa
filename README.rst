pysentosa - Python API for sentosa trading system
============================================================================================

- pysentosa is the Python API for sentosa trading system

- OS: Linux Ubuntu 15.04 64bit

- Installation: 

  ::

    sudo apt-get install -y python-pip libboost-all-dev libmysqlclient18 libyaml-cpp0.5
    sudo easy_install http://pypi.python.org/packages/2.7/p/pysentosa/pysentosa-0.1.13-py2.7.egg
    pip install pyyaml pymysql netifaces websocket-client nanomsg

- Launch your IB TWS.

- Run your strategy to trade

  Run demo:

  ::

    from pysentosa.demo import rundemo
    rundemo()

  Sample code:

  ::

    from pysentosa import Merlion, TT

    m = Merlion().run()
    target = 'SPY'
    m.track_msg(target)
    bounds = {target: [200, 250]}
    while True:
      symbol, ticktype, value = m.get_mkdata()
      if symbol == target:
        if ticktype == TT.ASK_PRICE and value < bounds[symbol][0]:
            m.buy(symbol, 100)
            bounds[symbol][0] -= 10
        elif ticktype == TT.BID_PRICE and value > bounds[symbol][1]:
            m.sell(symbol, 100)
            bounds[symbol][1] += 10

- FAQ:

  Q: How to fix "ERROR:Config account yyyyyy does not match IB account xxxxxx!"?
 
  A: Open ~/.sentosa/sentosa.yml and find account under global section, and replace the demo account with your own IB account.
