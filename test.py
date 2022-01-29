import time
import pyupbit

access = ""
secret = ""
upbit = pyupbit.Upbit(access, secret)

while True:
    time.sleep(0.165)
    if 1 == len(upbit.get_order("KRW-ETH")):
        time.sleep(0.250)
        a = upbit.get_order("KRW-ETH")[0]["uuid"]
        if a != upbit.get_order("KRW-ETH", state="done")[0]["uuid"]:
            b = upbit.get_order("KRW-ETH", state="done")[0]["uuid"]
            g = float(upbit.get_order(b)["trades"][0]["price"])
            e = round(g * 1.00266666667, -3)
            h = 6000/g
            i = round(g / 1.00266666667, -3)
            j = 6000/i
            upbit.sell_limit_order("KRW-ETH", e, h)
            upbit.buy_limit_order("KRW-ETH", i, j)
            upbit.cancel_order(a)
        elif a == upbit.get_order("KRW-ETH", state="done")[0]["uuid"]:
            b = upbit.get_order("KRW-ETH", state="done")[1]["uuid"]
            f = float(upbit.get_order(b)["trades"][0]["price"])
            k = round(f * 1.00266666667, -3)
            l = 6000/f
            n = round(f / 1.00266666667, -3)
            m = 6000/n
            upbit.sell_limit_order("KRW-ETH", k, l)
            upbit.buy_limit_order("KRW-ETH", n, m)
            upbit.cancel_order(a)
