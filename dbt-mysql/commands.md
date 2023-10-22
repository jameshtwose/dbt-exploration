## Setup MySQL Database
- https://dev.mysql.com/downloads/mysql/
- `ls /usr/local/mysql/bin` to check that mysql is installed
- `vim ~/.zshrc` and add the following to the end of the file:
    - `export PATH=$PATH:/usr/local/mysql/bin`
- `source ~/.zshrc` to source the file
- `mysql -u root -p` to connect to mysql (use the password you set up when installing mysql)
- `show databases;` to show the databases
- `create database hospital_B_ppe_data;` to create a database
- `use hospital_B_ppe_data;` to use the database
- `create table ppe_availability_hospital_B (id varchar(30) not null, category varchar(30) not null, product varchar(30) not null, number_of_units int null);` to create a table
- `show tables;` to show the tables
- `describe ppe_availability_hospital_B;` to describe the table
- `set global local_infile=true;` to allow local infile
- `exit` to exit mysql
- `mysql --local_infile=true -u root -p` to import the csv file into the table (make sure you are in the root directory of the project)
- go back to the mysql terminal and run the following:
    - `use hospital_B_ppe_data;`
    - `load data local infile 'data/MySQL_Dataset.csv' into table ppe_availability_hospital_B fields terminated by ',' enclosed by '"' lines terminated by '\n' ignore 1 rows;`
    - `select * from ppe_availability_hospital_B;` to check that the data has been imported
- `mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql -p` to import the timezone info into mysql (this is needed for the timestamp data type otherwise errors will occur)

## Setup dbt
- `pip install dbt-mysql` to install dbt-mysql (tested on python 3.9)
- https://docs.getdbt.com/quickstarts/manual-install?step=3 to install dbt
- `cd dbt-mysql` to go into the dbt-mysql directory
- `dbt init` to initialise dbt
- update the `~/.dbt/profiles.yml` file with the following:
```
ppe:
  target: dev
  outputs:
    dev:
      type: mysql
      server: localhost
      port: 3306  # optional
      database: hospital_B_ppe_data # optional, should be same as schema
      schema: hospital_B_ppe_data
      username: root
      password: Jq~gz^j2T?:Wt)7A
      driver: MySQL ODBC 8.0 ANSI Driver
    prod:
      type: mysql
      server: localhost
      port: 3306  # optional
      database: hospital_B_ppe_data # optional, should be same as schema
      schema: hospital_B_ppe_data
      username: root
      password: Jq~gz^j2T?:Wt)7A
      driver: MySQL ODBC 8.0 ANSI Driver    
```
- `cd ppe` to go into the ppe directory
- `dbt debug` to check that the connection to the database is working
- `dbt build` to build the dbt project
- `dbt run` to run the dbt project
- `dbt test` to test the dbt project
- `dbt docs generate` to generate the dbt docs
- `dbt docs serve` to serve the dbt docs locally (optional step - you can find the `index.html` file in the `target` directory)

## Serve docs to github pages
- `git checkout --orphan gh-pages` to create a new orphan branch called gh-pages
- copy paste everythin in the `target` directory into the `docs` directory
- `git add -f docs/*` to add the files in the target directory
- `git commit -m 'your commit messages' docs/*` to commit the files in the target directory
- `git push origin gh-pages` to push the files to the gh-pages branch
- `git checkout main` to go back to the main branch