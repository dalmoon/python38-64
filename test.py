import pyupbit

access = ""
secret = ""
upbit = pyupbit.Upbit(access, secret)

while True:
    if 1 == len(upbit.get_order("KRW-BTC")):
        a = upbit.get_order("KRW-BTC")[0]["uuid"]
        if a != upbit.get_order("KRW-BTC", state="done")[0]["uuid"] and 'bid' == upbit.get_order("KRW-BTC", state="done")[0]["side"]:
            b = upbit.get_order("KRW-BTC", state="done")[0]["uuid"]
            g = float(upbit.get_order(b)["trades"][0]["price"])
            e = round(g * 1.00266666667, -3)
            h = 6000/g
            i = round(g / 1.00266666667, -3)
            j = 6000/i
            upbit.sell_limit_order("KRW-BTC", e, h)
            upbit.buy_limit_order("KRW-BTC", i, j)
            upbit.cancel_order(a)
        elif a == upbit.get_order("KRW-BTC", state="done")[0]["uuid"]:
            b = upbit.get_order("KRW-BTC", state="done")[1]["uuid"]
            f = float(upbit.get_order(b)["trades"][0]["price"])
            k = round(f * 1.00266666667, -3)
            l = 6000/f
            n = round(f / 1.00266666667, -3)
            m = 6000/n
            upbit.sell_limit_order("KRW-BTC", k, l)
            upbit.buy_limit_order("KRW-BTC", n, m)
            upbit.cancel_order(a)
