# Comments
1. I assumed the app should be built using given (not the latest) version of the packages.
2. The repositores are not using `litestar_asyncpg` pool, it would require to rewrite Repos and Services and make them using connection instead of session.
3. So the connection created by `litestar_asyncpg` is used for direct db access in `health_check` endpoint.

# Challenges Faced
- Make alembic migration to use async driver.
- `advanced_alchemy` is not the latest so `PasswordHash` is copied from the latest version and hashing backend implemented without 3rd packages. The password can be check using `check_password` endpoint.