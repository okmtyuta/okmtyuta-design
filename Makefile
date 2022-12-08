run-local-makemigrations:
	echo "マイグレーションファイルを作成します"
	python3 manage.py makemigrations
run-local-migrate:
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
build-database:
	echo "データベースのビルドを行います"
	docker-compose build database
run-database:
	echo "データベースを起動します"
	docker-compose up database

run-makemigrations:
	@echo "マイグレーションファイルを作成します"
	docker compose exec okmtyuta-design python3 manage.py makemigrations
run-migrate:
	@echo "マイグレーションファイルを作成します"
	docker compose exec okmtyuta-design python3 manage.py migrate
run-test:
	docker-compose exec okmtyuta-design gunicorn --bind '0.0.0.0:8001' --chdir /app config.wsgi
	# docker-compose exec okmtyuta-design python3 manage.py runserver 0.0.0.0:8001
