import pybithumb
import time

"""
<빗썸에서 거래되는 비트코인의 코드들>
tickers = pybithumb.get_tickers()
print(tickers)
"""

#== 현재가 얻기 ==#
# 빗썸의 공개 API는 초당 20회 호출할 수 있습니다. #
while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(1)
