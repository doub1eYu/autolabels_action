# githubラベル自動化
githubのラベル管理を自動化、かつ一元化するためのアクション。
## 初回実行  
1. labels_custom.tomlに追加したいラベル情報を編集。  
2. labels_custom.tomlとlabels_first_time.tomlを.githubの下に格納。  
3. フォルダ構成は下記のようになった上、.githubフォルダをマスタブランチにプッシュする。  
<pre>
.github  
 |--workflows  
 |  |--labels.yml                → githubアクション定義ファイル
 |--fetch_labels.py              → バッチファイル  
 |--labels.toml                  → ラベル管理定義ファイル（初回の時、中身は関係なし）  
 |--labels_custom.toml           → 初期設定で追加したいラベルの定義ファイル（初回実行後は自動的に削除）
 |--labels_first_time.toml       → 初期設定で変換したいgithubデフォルトラベルの定義ファイル（初回実行後は自動的に削除）
</pre>   

## バッチ動き説明  
* 初回実行の場合、githubデフォルトラベルを日本語に変換し、デフォルトラベル以外のラベルは変更なし。
* 初回以降の場合、
  * githubアクション定義ファイル「labels.yml」を編集することより、ラベルを更新。
  * githubコンソール画面でラベルを修正、「labels.yml」も自動で更新される。
