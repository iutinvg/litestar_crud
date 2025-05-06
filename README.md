# Comments
1. I assumed the app should be built using given (not the latest) version of the packages.
2. The repositores are not using `litestar_asyncpg` pool, it would require to rewrite Repos and Services and make them using connection instead of session.
3. So the connection created by `litestar_asyncpg` is used for direct db access in `health_check` endpoint.

# Challenges Faced
- Make alembic migration to use async driver.
- `advanced_alchemy` is not the latest so `PasswordHash` is copied from the latest version and hashing backend implemented without 3rd packages. The password can be check using `check_password` endpoint.

# How to Run
Requirements
- Python 3.12
- Poetry installed
- Docker installed

Linux/Mac:
1. `git clone git@github.com:iutinvg/litestar_crud.git`
2. `cd litestar_crud`
3. `python -m venv venv`
4. `source venv/bin/activate`
5. `poetry install`
6. `make dbup`
7. `make dbmigrate`
8. `make run`
9. open `http://localhost:8000/schema/swagger`
