run-makemigrations:
	echo "マイグレーションファイルを作成します"
	python3 manage.py makemigrations
run-migrate:
	echo "マイグレーションファイルを作成します"
	python3 manage.py migrate
runserver:
	echo "開発用サーバーを起動します"
	python3 manage.py runserver 8001
build:
	echo "okmtyuta-designのビルドを行います"
	docker-compose build okmtyuta-design
run:
	echo "okmtyuta-designを起動します"
	docker-compose up okmtyuta-design
