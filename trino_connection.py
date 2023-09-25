# %%
from trino.dbapi import connect

# %%
conn = connect(
    host="0.0.0.0",
    port="8080",
    user="admin",
    # catalog="<catalog>",
    # schema="<schema>",
)
# %%
cur = conn.cursor()
cur.execute("SELECT * FROM system.runtime.nodes")
rows = cur.fetchall()
rows
# %%
cur.execute("select count(*) from tpch.sf1.nation")
rows = cur.fetchall()
rows
# %%
cur.close()
# %%
conn.close()
# %%
