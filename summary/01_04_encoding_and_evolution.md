- [myriad](https://www.oxfordlearnersdictionaries.com/definition/english/myriad_1)

- [instantiate](https://dictionary.cambridge.org/ja/dictionary/english/instantiate)

- [afterthought](https://dictionary.cambridge.org/ja/dictionary/english/afterthought)

- [bloated](https://dictionary.cambridge.org/ja/dictionary/english/bloated)

- [transient](https://dictionary.cambridge.org/ja/dictionary/english/transient)

- [work around](https://dictionary.cambridge.org/ja/dictionary/english/work-around)

- [hacky](https://dictionary.cambridge.org/ja/dictionary/english/hacky)

- [hardcode](https://dictionary.cambridge.org/ja/dictionary/english/hardcode)

- fairly

- don't bother doing: わざわざ~しない

- [lowest common denominator](https://dictionary.cambridge.org/dictionary/english/lowest-common-denominator)

- [negligible](https://dictionary.cambridge.org/dictionary/english/negligible)

- [thrift](https://dictionary.cambridge.org/dictionary/english/thrift)
    - [thief](https://dictionary.cambridge.org/dictionary/english/thief)

- [concatenation](https://dictionary.cambridge.org/ja/dictionary/english/concatenation)

- [truncated](https://dictionary.cambridge.org/ja/dictionary/english/truncated)

- [gloss over](https://dictionary.cambridge.org/ja/dictionary/english/gloss-over?q=gloss+over+something)

- [aforementioned](https://dictionary.cambridge.org/ja/dictionary/english/aforementioned)

- [propriety](https://dictionary.cambridge.org/ja/dictionary/english/proprietary)

- [viable](https://dictionary.cambridge.org/ja/dictionary/english/viable)

- [snag](https://dictionary.cambridge.org/ja/dictionary/english/snag)

- [in one go](https://eow.alc.co.jp/search?q=in+one+go)

- [misnomer](https://dictionary.cambridge.org/ja/dictionary/english/misnomer)

- [oath](https://qiita.com/TakahikoKawasaki/items/e37caf50776e00e733be)

- [sprawling](https://dictionary.cambridge.org/ja/dictionary/english/sprawling)

- [ostensibly](https://dictionary.cambridge.org/ja/dictionary/english/ostensibly)

- https://aws.amazon.com/jp/compare/the-difference-between-soap-rest/

- [incarnation of sth](https://dictionary.cambridge.org/ja/dictionary/english/incarnation)

- [deduplication](https://e-words.jp/w/%E9%87%8D%E8%A4%87%E6%8E%92%E9%99%A4.html)

- [encapsulate](https://dictionary.cambridge.org/ja/dictionary/english/encapsulate)

- [pitfall](https://dictionary.cambridge.org/ja/dictionary/english/pitfall)



https://aws.amazon.com/jp/compare/the-difference-between-rpc-and-rest/

https://cloud.google.com/blog/ja/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them

- I think there is no explanation about difference between REST and RPC in this book, so I asked ChatGPT.

(ChatGPT)

REST（Representational State Transfer）とRPC（Remote Procedure Call）は、異なるアプローチでリモート通信を実現するための2つの異なるコンセプトです。以下は、それぞれの特徴を簡潔に示した表です。

| 概要                  | REST                                      | RPC                                |
|-----------------------|-------------------------------------------|------------------------------------|
| アーキテクチャスタイル | シンプルでステートレスなアーキテクチャ | リモートメソッド呼び出しを中心とする  |
| プロトコル            | HTTP                                      | カスタムまたはSOAPなどのプロトコル |
| リソース指向         | リソース（データ）に基づいたアプローチ   | メソッド（関数）呼び出しを中心とする  |
| URLデザイン           | リソースごとに一意のURL                  | エンドポイントごとにメソッドを指定    |
| メッセージ形式       | JSON、XML、HTMLなど                      | カスタム、XML、JSONなど              |
| ステート             | ステートレス                            | ステートフルまたはステートレス      |
| キャッシュ           | レスポンスに対するキャッシュをサポート | 一般的にキャッシュはサポートされない |

要するに、RESTはHTTPプロトコルを基にし、リソースを操作するためのアーキテクチャスタイルで、主にデータの取得、作成、更新、削除（CRUD操作）に適しています。一方、RPCはリモートで関数やメソッドを呼び出すことを中心にしたアプローチで、より柔軟なリモート操作が可能ですが、プロトコルはHTTP以外も含めて選択できます。どちらを選ぶかは、特定のプロジェクトや要件に依存します。

