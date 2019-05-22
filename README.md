# LINE bot APIでimage mapを作る時用の自動化ツール

LINE bot の imagemap APIを使う際の画像を用意します。

imagemapの詳細は[こちらのQiitaの記事](https://qiita.com/nao-guitarist/items/519dc9e513371eaf7b46)が詳しい。
ようは画像を5種類用意しなきゃなんだけど、一枚画像を用意すれば、自動的にimagemapで使えるに変換してくれる。

動作の際に`OpenCV`が必要になるので、入れておく。

`python app.py`

で動作させる。

`save`にいくつpngファイルを入れても大丈夫だが、少し重い処理。
