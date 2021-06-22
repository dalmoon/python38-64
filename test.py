

import pyupbit
import time

access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

a = upbit.get_order("KRW-ETH")[0]["uuid"] # 매수 UUID
b = upbit.get_order("KRW-ETH")[1]["uuid"] # 매도 UUID
d = 6000 # 6000원


while True:
    #c = len(upbit.get_order("KRW-ETH")) #미체결 건 수
    if 1 == len(upbit.get_order("KRW-ETH")):
        if a == upbit.get_order("KRW-ETH")[0]["uuid"]:
            #print("a에 들어옴")
            upbit.cancel_order(a)
            g = float(upbit.get_order(b)["trades"][0]["price"]) # 매도 금액
            e = round(g * 1.00266666667, -3) # 매도가격
            h = 6000/g # 매도주문수량
            i = round(g / 1.00266666667, -3) # 매수가격
            j = 6000/i # 매수주문수량
            upbit.sell_limit_order("KRW-ETH", e, h)
            upbit.buy_limit_order("KRW-ETH", i, j)
            #time.sleep(0.001)
            if 2 == len(upbit.get_order("KRW-ETH")):
                a = upbit.get_order("KRW-ETH")[0]["uuid"] # 매수 UUID
                b = upbit.get_order("KRW-ETH")[1]["uuid"] # 매도 UUID
                #print("uuid 2개")
            else:
                a = upbit.get_order("KRW-ETH", state="done")[0]["uuid"]
                b = upbit.get_order("KRW-ETH")[0]["uuid"] # 매수 UUID
                #print("바로 체결?")
        elif b == upbit.get_order("KRW-ETH")[0]["uuid"]:
            #print("b에 들어옴")
            upbit.cancel_order(b)
            f = float(upbit.get_order(a)["trades"][0]["price"]) # 매수 금액
            k = round(f * 1.00266666667, -3) # 매도가격
            l = 6000/f # 매도주문수량
            n = round(f / 1.00266666667, -3) # 매수가격
            m = 6000/n # 매수주문수량
            upbit.sell_limit_order("KRW-ETH", k, l)
            upbit.buy_limit_order("KRW-ETH", n, m)
            #time.sleep(0.001)
            if 2 == len(upbit.get_order("KRW-ETH")):
                a = upbit.get_order("KRW-ETH")[0]["uuid"] # 매수 UUID
                b = upbit.get_order("KRW-ETH")[1]["uuid"] # 매도 UUID
                #print("uuid 2개")
            else:
                a = upbit.get_order("KRW-ETH", state="done")[0]["uuid"]
                b = upbit.get_order("KRW-ETH")[0]["uuid"] # 매수 UUID
                #print("바로 체결?")
    #time.sleep(0.001)
