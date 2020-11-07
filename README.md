# ・アプリ名
## pythonアウトプット日記（使用言語： python, フレームワーク：　Django）

# ・概要
## Django管理サイトから入り、タイトル名・本文・カテゴリ（学習した言語名）・タグ（参考テキスト名）を入力し、学習した内容のアウトプットを目的としたアプリとなっています。

# ・制作背景（意図）
## 自分用のアウトプット用サイトを作成し、日々インプットしている内容を定着させる事ができるようにしたいと思った事がきっかけです。また、後から見返した際アウトプットの内容がどの参考テキストに記載されているのかも把握出来るようにしたかったため、タグ名が参考テキスト名になります。

# ・DEMO
## https://gyazo.com/96d2e21ea4ac5cb813ae3b3697152875

# ・DB設計
## Tagモデル

|Column|field|options|
|------|-----|-------|
|name|models.CharField|'タグ名', max_length=255|


## Categoryモデル

|Column|field|options|
|------|-----|-------|
|name|models.CharField|'カテゴリ名', max_length=255|


## Postモデル

|Column|field|options|
|------|-----|-------|
|title|models.CharField|'タイトル名', max_length=30|
|text|models.TextField|'本文'|
|category|models.ForeignKey|Category, on_delete=models.PROTECT, verbose_name='カテゴリ'|
|tags|models.ManyToManyField|Tag, verbose_name='タグ', blank=True|
|created_at|models.DateTimeField|'学習日', auto_now_add=True|
|updated_at|models.DateTimeField|'更新日', auto_now=True|
