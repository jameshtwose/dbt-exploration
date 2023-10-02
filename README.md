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

## Usage (local - docker + trino)
- `docker run --name trino -d -p 8080:8080 --volume ./etc/trino:/etc/trino trinodb/trino`
- `docker run --name trino -d -p 8080:8080 trinodb/trino`
- `docker ps` - check that the container is running (check healthy)
- `docker exec -it trino trino --server localhost:8080 --catalog tpch --schema sf1`
- `docker exec -it trino trino`
- `select count(*) from tpch.sf1.nation;`

## Usage (local - docker + kubernetes/ minikube + trino + postgres + kafka + zookeeper)
- `minikube start`
- `minikube dashboard`
- install [helm](https://helm.sh/docs/intro/install/)
    - `brew install helm`
- `helm repo add bitnami https://charts.bitnami.com/bitnami`
- `helm search repo bitnami`
- `helm install new-mysql bitnami/mysql`
- get the password
    - `kubectl get secret --namespace default new-mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode`
- run a pod that you can use as a client
    - `kubectl run new-mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.34-debian-11-r56 --namespace default --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash`
- connect to mysql
    - `mysql -h new-mysql.default.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD"`
    - `show databases;`
    - `use mysql;`
    - `show tables;`
    - `select * from user;`
    - `exit`
    - leave the pod
        - `exit`
- `helm install new-postgres bitnami/postgresql`
- get the password
    - `kubectl get secret --namespace default new-postgres-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d`
    - `export POSTGRES_PASSWORD=$(kubectl get secret --namespace default new-postgres-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)`
- run a pod that you can use as a client
    - `kubectl run new-postgres-postgresql-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:16.0.0-debian-11-r3 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host new-postgres-postgresql -U postgres -d postgres -p 5432`
    - `select * from pg_catalog.pg_tables;`
    - `exit`
    - `kubectl port-forward --namespace default svc/new-postgres-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432`
    - `select * from pg_catalog.pg_tables;`


## Demo
- `dbt init` - create a new dbt project
- `mf tutorial` - run the dbt tutorial


