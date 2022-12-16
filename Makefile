build-okmtyuta-design:
	echo "okmtyuta-designのビルドを行います"
	@docker-compose build okmtyuta-design
run-okmtyuta-design:
	echo "okmtyuta-designを起動します"
	@docker-compose up -d okmtyuta-design
build-database:
	echo "データベースのビルドを行います"
	@docker-compose build database
run-database:
	echo "データベースを起動します"
	@docker-compose up -d database

run-makemigrations:
	echo "マイグレーションファイルを作成します"
	@docker-compose exec okmtyuta-design python3 manage.py makemigrations
run-migrate:
	echo "マイグレートを実行します"
	@docker-compose exec okmtyuta-design python3 manage.py migrate
runserver:
	echo "サーバーを起動します"
	@docker-compose exec okmtyuta-design gunicorn --bind '0.0.0.0:8002' --chdir /app config.wsgi
	# docker-compose exec okmtyuta-design python3 manage.py runserver 0.0.0.0:8002
