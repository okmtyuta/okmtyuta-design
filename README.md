# okmtyuta Design Documentation

## 使用中のポート

| 使用するサービス | ポート番号 |
| ---------------- | ---------- |
| okmtyuta-design  | 8001       |
| postgresql       | 4001       |

### .env ファイルを用意する

.env ファイルをルートディレクトリに作成する。.env ファイルに書く必要があることは以下の通り。

- `DJANGO_SETTINGS_MODULE`: 読み込む setting ファイルの指定。`config.settings.local || config.settings.production`
- `SECRET_KEY`: シークレットキー
- `OKMTYUTA_DESIGN_PORT`: サービスのポート番号
- `DATABASE_TYPE`: データベースの種類。`sqlite || postgresql`
- `POSTGRES_DB`: Postgresのテーブル名
- `POSTGRES_USER`: Postgresのユーザー名
- `POSTGRES_PASSWORD`: Postgresのパスワード
- `POSTGRES_PORT`: Postgresのポート番号

### Migrate

ルートディレクトリで以下のコマンドを実行する。

- `make run-makemigrations`
- `make run-migrate`

### 配信を開始する

### 開発用サーバーを起動する

以下のコマンドにより開発用サーバーを起動できる（ポート番号 8001 で起動することに注意）。

- `make runserver`

---

### Visual Studio Code 用のセッティング

`.vscode/setting.json`
```json
{
  "cSpell.words": ["dotenv", "makemigrations", "okmtyuta", "runserver"]
}
```
