import time
import pyupbit

access = ""
secret = ""
upbit = pyupbit.Upbit(access, secret)

while True:
    time.sleep(4.000)
    if 0 < len(upbit.get_order("KRW-ETH")):
        time.sleep(1.000)
        a = upbit.get_order("KRW-ETH")[0]
        if a["side"] == 'bid':
            g = float(a["price"])
            e = round(g * 1.00266666667, -3)
            e = round(e * 1.00266666667, -3)
            e = round(e * 1.00266666667, -3)
            h = 6000/round(e / 1.00266666667, -3)
            i = round(g * 1.00266666667, -3)
            j = 6000/i
            upbit.sell_limit_order("KRW-ETH", e, h)
            upbit.buy_limit_order("KRW-ETH", i, j)
            upbit.cancel_order(a["uuid"])
        else:
            f = float(a["price"])
            k = round(f / 1.00266666667, -3)
            l = 6000/round(k / 1.00266666667, -3)
            n = round(f / 1.00266666667, -3)
            n = round(n / 1.00266666667, -3)
            n = round(n / 1.00266666667, -3)
            m = 6000/n
            upbit.sell_limit_order("KRW-ETH", k, l)
            upbit.buy_limit_order("KRW-ETH", n, m)
            upbit.cancel_order(a["uuid"])
