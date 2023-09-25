# dbt-exploration
A repo of Jms' exploration into dbt.

## Setup
Based on dbt + trino with a streamlit frontend.
- [Trino](https://trino.io/) is a distributed SQL query engine for big data analytics.
- [dbt](https://www.getdbt.com/) is a tool that enables data analysts and engineers to transform data in their warehouse more effectively.
- [streamlit](https://streamlit.io/) is an open-source app framework for Machine Learning and Data Science teams.
- [Trino episode 21](https://trino.io/episodes/21.html)
- [Trino + dbt Demo](https://github.com/victorcouste/trino-dbt-demo)

![trino+dbt](images/dbt-trino-architecture.png)

## Usage
- `docker run --name trino -d -p 8080:8080 --volume ./etc/trino:/etc/trino trinodb/trino`
- `docker run --name trino -d -p 8080:8080 trinodb/trino`
- `docker ps` - check that the container is running (check healthy)
- `docker exec -it trino trino --server localhost:8080 --catalog tpch --schema sf1`
- `docker exec -it trino trino`
- `select count(*) from tpch.sf1.nation;`

## Demo
- `dbt init` - create a new dbt project
- `mf tutorial` - run the dbt tutorial
