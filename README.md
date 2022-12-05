# okmtyuta Design Documentation

## 使用中のポート
|  使用するサービス  |  ポート番号  |
| ---- | ---- |
|  okmtyuta-design  |  8001  |
|  postgresql  |  4001  |

### .envファイルを用意する
.envファイルをルートディレクトリに作成する。.envファイルに書く必要があることは以下の通り。
  - `DJANGO_SETTINGS_MODULE`: 読み込むsettingファイルの指定。`config.settings.local || config.settings.production`
  - `SECRET_KEY`: シークレットキー

### Migrate
ルートディレクトリで以下のコマンドを実行する。
  - `make run-makemigrations`
  - `make run-migrate`

### 配信を開始する

### 開発用サーバーを起動する
以下のコマンドにより開発用サーバーを起動できる（ポート番号8001で起動することに注意）。
  - `make run-start-dev`