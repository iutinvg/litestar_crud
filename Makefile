run:
	granian --interface asgi crud/main:app --reload

dbup: dbdown
	docker compose up db --detach

dbdown:
	docker compose down db

dbmigrate:
	alembic upgrade head

psql:
	docker exec -it $(shell docker ps -q -f name=db) psql -Upostgres crud_db
