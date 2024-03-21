# CommonCrawlのPDFデータ(日本語)をダウンロードするScript

# 使い方
- 以下のコマンドを実行すると､dataフォルダ内に､日本ドメインのpdfファイルがダウンロードされていきます｡
 - 1. 日本語pdfの多そうなzipファイルをダウンロード
 - 2. zipを展開し､.jpドメイン以外のpdfを削除
 - 3. 1.に戻る
~~~
mkdir data
python download.py
~~~

#ファイルリストのダウンロード (日本語ドメイン以外も使う場合のみ､実行)
- 日本語のファイルリストは[こちら](./ja_df.csv)
~~~
mkdir data
cd data

#download file list
wget https://digitalcorpora.s3.amazonaws.com/corpora/files/CC-MAIN-2021-31-PDF-UNTRUNCATED/metadata/cc-hosts-20230303.csv.gz

gzip -d cc-hosts-20230303.csv.gz

#その後､適当にドメインを抽出する処理を加える
~~~