#== 호가 정보 ==#
import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']  #매수호가
asks = orderbook['asks']  #매도호가

for bid in bids:
    price = bid['price']
    quantity = bid['quantity']
    print("매수호가 : ", price, "매수잔량 : ", quantity)

for ask in asks:
    price = ask['price']
    quantity = ask['quantity']
    print("매도호가 : ", price, "매도잔량 : ", quantity)