# pysentosa
The smallest algorithmic trading system in the world

```
  from pysentosa.merlion import *
  
  m = Merlion().run()
  target = 'SPY'
  m.track_msg(target)
  bounds = {target: [200, 250]}
  while True:
    symbol, ticktype, value = m.get_mkdata()
    if symbol == target:
      print symbol, ticktype, value
      if ticktype == ASK_PRICE and value < bounds[symbol][0]:
          m.buy(symbol, 100)
          bounds[symbol][0] -= 10
      elif ticktype == BID_PRICE and value > bounds[symbol][1]:
          m.sell(symbol, 100)
          bounds[symbol][1] += 10
```
