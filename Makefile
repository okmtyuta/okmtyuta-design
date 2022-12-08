build-okmtyuta-design:
	echo "okmtyuta-designのビルドを行います"
	docker-compose build okmtyuta-design
run-okmeyuta-design:
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
	@echo "マイグレートを実行します"
	docker compose exec okmtyuta-design python3 manage.py migrate
runserver:
	@echo "サーバーを起動します"
	docker-compose exec okmtyuta-design gunicorn --bind '0.0.0.0:8001' --chdir /app config.wsgi
	# docker-compose exec okmtyuta-design python3 manage.py runserver 0.0.0.0:8001
