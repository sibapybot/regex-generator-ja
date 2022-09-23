# regex-generator-ja
日本語に特化した正規表現ジェネレーターです。

# 使用ライブラリ
```
MeCab
```
MeCabのお茶選を使用しています。  
MeCabの辞書はproces.pyを書き換えることで変更できます。

# 使い方
例
```py
import generator,math

#正規表現の作成
texts = ["testだあああああああ！！！agfnl545sad testだあああああああ！！！arf testだあああああああ！！！","testだあああああああ！！！testだあああああああ！！！testだあああああああ！！！","testだあああああああ！！！a testだあああああああ！！！arf  adfs testだあああああああ！！！"]
ragex = generator.create()

#一致しているかどうかの判定
text = "testだあああああああ！！！agfnl545sad testだあああああああ！！！arf testだあああああああ！！！"
print(math.regex_ja_match(text,ragex))
#出力(bool値)
#True
```
