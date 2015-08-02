from pysentosa import Merlion, TT

def rundemo():
  s='''m = Merlion().run()
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
        bounds[symbol][1] += 10'''
  print '*'*80
  print s
  print '*'*80
  exec(s)

if __name__ == '__main__':
  rundemo()
