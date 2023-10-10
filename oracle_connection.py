# %%
from sqlalchemy import create_engine, text
import pandas as pd
import oracledb

# %%
# Set up the connection string
username = 'C##jms'
password = 'mypassword'
hostname = 'localhost'
port = '1530'
# service_name = 'ORCL'
service_name = "FREE"

# connection_string = f'oracle://{username}:{password}@{hostname}:{port}/{service_name}'
# oracle+oracledb://user:pass@hostname:port[/dbname][?service_name=<service>[&key=value&key=value...]]

connection_string = f'oracle+oracledb://{username}:{password}@{hostname}:{port}/{service_name}'

print(connection_string)

# %%
# connection_string = f"{hostname}:{port}/{service_name}"
# c = oracledb.connect(user=username, password=password, dsn=connection_string)

# %%
# Create the engine and connect to the database
engine = create_engine(connection_string)

with engine.connect() as connection:
    # Query the database and read the results into a pandas dataframe
    query = text('select * from C##jms.test')
    df = pd.read_sql(query, connection)

# %%
df
# %%
