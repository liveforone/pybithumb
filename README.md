<h2>main - 고유코드</h2>
<pre>
가상화폐에 주식처럼 고유 코드를 사용하는데 이를 ticker라 한다. (ex: BTC)
</pre>

<h2>main2 - 거래 정보</h2>
<pre>
24시간 동안의 시가/고가/저가/종가/거래량 을 get_market_detail이 반환
</pre>

<h2>main3 - 호가 정보</h2>
<pre>
변수 - get_orderbook("BTC")로 호가 정보를 불러온다.
인덱싱으로 변수['bids'] -> 매수호가 / 변수['asks'] -> 매도호가 를 불러온다.
</pre>