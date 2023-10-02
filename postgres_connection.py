# %%
from sqlalchemy import create_engine
from sqlalchemy import text

# %%
# postgresql+psycopg2://user:password@hostname/database_name
engine = create_engine("postgresql://postgres:2JNAAcVQMt@localhost:5432")
# %%
with engine.connect() as conn:
    response = conn.execute(
        text(
            """
                      SELECT datname FROM pg_database
                        WHERE datistemplate = false;
                      """
        )
    )
    print(response.fetchall())
# %%
engine = create_engine("postgresql://postgres:2JNAAcVQMt@localhost:5432/postgres")
# %%
with engine.connect() as conn:
    response = conn.execute(
        text(
            """SELECT * FROM pg_catalog.pg_tables;"""
        )
    )
    print(response.fetchall())
# %%
# create new table
with engine.connect() as conn:
    response = conn.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INTEGER NOT NULL
            );
            """
        )
    )

# %%
# insert data
with engine.connect() as conn:
    response = conn.execute(
        text(
            """
            INSERT INTO test_table (name, age) VALUES ('John', 25);
            """
        )
    )

# %%
with engine.connect() as conn:
    response = conn.execute(
        text(
            """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';            """
        )
    )
    print(response.fetchall())
# %%
