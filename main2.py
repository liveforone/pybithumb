#== 거래 정보 ==#
import pybithumb

detail = pybithumb.get_market_detail("BTC")
print(detail)