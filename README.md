# LIDAR_M1C1_mini_python_loder

国科光芯（海宁）科技股份有限公司にて作られたM1C1_miniの点群データの取得、計算、表示をするプログラムです。
実行環境を構築する際にはvenvにて仮想環境を構築し、`pip install -r requirements.txt`を実行していただければと思います。


LIDARをPCに接続すると勝手に点群データを送信してくれるため、接続しているPCのポートだけ書き換えて`python testSerial.py`を
実行すると取得した点群データをmatplotlibにて見える化してくれます。


# 入手先
https://www.aliexpress.com/i/4000251359842.html

# 仕様書
- http://www.cspctech.com/Service/index/cate_id/3

# 参考にしたページ
点群データをシリアルから読み取るコードを書くにあたって参考にしました。感謝です。
- https://ameblo.jp/sy-eng/entry-12597655892.html
