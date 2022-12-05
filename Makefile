run-makemigrations:
	echo "マイグレーションファイルを作成します"
	python3 manage.py makemigrations
run-migrate:
	echo "マイグレーションファイルを作成します"
	python3 manage.py migrate
run-start-dev:
	echo "開発用サーバーを起動します"
	python3 manage.py runserver 8001

