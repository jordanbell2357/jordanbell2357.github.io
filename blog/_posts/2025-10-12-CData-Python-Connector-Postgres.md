---
layout: post
title: CData Python Connector for Postgres
topic: python
---

<https://www.cdata.com/developers/python/#pythonsources>

<https://www.cdata.com/developers/article/python/dev-guide-getting-started/>

## CSV Connector

```bash
unzip CDataPythonConnectorforCSV.zip

cd CData.Python.CSV/

python3.13 -m venv venv/ --prompt .

source venv/bin/activate

python -m pip install cdata-csv-connector-25.0.9376-python3.tar.gz
```

Then we go to the virtual environment site-packages directory, which we determine with

```console
(CData.Python.CSV) ubuntu@LAPTOP-JBell:~/CData.Python.CSV/venv/lib/python3.13/site-packages$ python -m site
sys.path = [
    '/home/ubuntu/CData.Python.CSV/venv/lib/python3.13/site-packages',
    '/usr/lib/python313.zip',
    '/usr/lib/python3.13',
    '/usr/lib/python3.13/lib-dynload',
]
USER_BASE: '/home/ubuntu/.local' (exists)
USER_SITE: '/home/ubuntu/.local/lib/python3.13/site-packages' (doesn't exist)
ENABLE_USER_SITE: False
```

```bash
cd venv/lib/python3.13/site-packages/cdata/installlic_csv

./install-license.sh
```


```python3
import cdata.csv as mod  # Import CData CSV module

# Get and validate CSV directory path 
csv_path = "/home/ubuntu/CData.Python.CSV"

# Reconnect to the CSV engine to fetch available stored procedures 
conn = mod.connect(f"URI={csv_path}") 
 
cur = conn.cursor() 

cur.execute("SELECT * FROM sys_tables") 
 
for row in cur.fetchall(): 
    print(row)
```

```
(CData.Python.CSV) ubuntu@LAPTOP-JBell:~/CData.Python.CSV$ /home/ubuntu/CData.Python.CSV/venv/bin/python /home/ubuntu/CData.Python.CSV/cdata_csv_connector.py
('CData', 'CSV', 'Account.csv', 'TABLE', None, True, False)
('CData', 'CSV', 'license.txt', 'TABLE', None, True, False)
('CData', 'CSV', 'Opportunity.csv', 'TABLE', None, True, False)
('CData', 'CSV', 'readme.txt', 'TABLE', None, True, False)
```

```python3
import cdata.csv as mod  # Import CData CSV module

# Get and validate CSV directory path 
csv_path = "/home/ubuntu/CData.Python.CSV"

# Reconnect to the CSV engine to fetch available stored procedures 
conn = mod.connect(f"URI={csv_path}") 
 
cur = conn.cursor() 

cur.execute("SELECT * FROM sys_tablecolumns WHERE TableName = 'Account.csv' LIMIT 5;")
 
for column in cur.fetchall():
    print(column)
```

```
(CData.Python.CSV) ubuntu@LAPTOP-JBell:~/CData.Python.CSV$ /home/ubuntu/CData.Python.CSV/venv/bin/python /home/ubuntu/CData.Python.CSV/cdata_csv_connector.py
('CData', 'CSV', 'Account.csv', 'Id', 12, 'VARCHAR', 2000, 2000, 0, True, 'This is a generated column, no description is available.', 0, False, False, False, False, 0, False, False, None)
('CData', 'CSV', 'Account.csv', 'IsDeleted', 16, 'BIT', 1, 1, 0, True, 'This is a generated column, no description is available.', 1, False, False, False, False, 1, False, False, None)
('CData', 'CSV', 'Account.csv', 'MasterRecordId', 12, 'VARCHAR', 2000, 2000, 0, True, 'This is a generated column, no description is available.', 2, False, False, False, False, 0, False, False, None)
('CData', 'CSV', 'Account.csv', 'Name', 12, 'VARCHAR', 2000, 2000, 0, True, 'This is a generated column, no description is available.', 3, False, False, False, False, 0, False, False, None)
('CData', 'CSV', 'Account.csv', 'Type', 12, 'VARCHAR', 2000, 2000, 0, True, 'This is a generated column, no description is available.', 4, False, False, False, False, 0, False, False, None)
```


```python3
import cdata.csv as mod  # Import CData CSV module

# Get and validate CSV directory path 
csv_path = "/home/ubuntu/CData.Python.CSV"

# Reconnect to the CSV engine to fetch available stored procedures 
conn = mod.connect(f"URI={csv_path}") 
 
cur = conn.cursor() 

cur.execute("SELECT * FROM Account LIMIT 1;")
 
for r in cur.fetchall():
    print(r)
```

```
(CData.Python.CSV) ubuntu@LAPTOP-JBell:~/CData.Python.CSV$ /home/ubuntu/CData.Python.CSV/venv/bin/python /home/ubuntu/CData.Python.CSV/cdata_csv_connector.py
('0016A000003FZabQAG', False, '', 'Edge Communications, Inc.', 'Customer - Direct', '', '312 Constitution Place', 'Austin', 'TX', 78767, 'USA', '', '', '', '312 Constitution Place', 'Houston', 'TX', 78767, 'USA', '', '', '', '(512) 757-6000', '(512) 757-9000', 'CD451796', 'http://edgecomm.com', '/services/images/photo/0016A000003FZabQAG', 6576, 'Electronics', 139000000, 1000, 'Public', 'EDGE', 'Edge, founded in 1998, is a start-up based in Austin, TX. The company designs and manufactures a device to convert music from one digital format to another. Edge sells its product through retailers and its own website.', 'Hot', '', '0056A000000n1ErQAI', datetime.datetime(2017, 5, 12, 8, 1, 24), '0056A000000n1ErQAI', datetime.datetime(2021, 5, 28, 11, 20, 52), '0056A0000025m9dQAA', datetime.datetime(2021, 5, 28, 11, 20, 52), '', '', '', '', '', 'Pending', '', '', '', '', '', '', '', '', 'Medium', 'Silver', 'Yes', 2, 'Maybe', 2657, datetime.date(2017, 6, 6), '')
```



## Postgres Connector

### Install Postgres and make table

Install Postgres:

```bash
sudo apt install postgresql

sudo systemctl start postgresql

sudo systemctl enable postgresql
```

```
ubuntu@LAPTOP-JBell:~$ nmap localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-10-12 20:32 EDT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000069s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
25/tcp   open  smtp
631/tcp  open  ipp
5432/tcp open  postgresql

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

```
ubuntu@LAPTOP-JBell:~$ sudo -u postgres psql
psql (14.18 (Ubuntu 14.18-0ubuntu0.22.04.1), server 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# ALTER USER postgres PASSWORD 'postgres';
ALTER ROLE
postgres=# \q
```

Then

```bash
sudo vi sudo vi /etc/postgresql/14/main/pg_ident.conf
```

Change

```
# Database administrative login by Unix domain socket
local   all             postgres                                peer
```

to

```
# Database administrative login by Unix domain socket
local   all             postgres                                md5
````

Then

```bash
sudo systemctl restart postgresql
```

### Using CData Python Connector for Postgres

<https://cdn.cdata.com/help/FPM/py/>

Download CData Postgres Connector for Python: <https://www.cdata.com/developers/python/>

```bash
unzip CDataPythonConnectorforPostgreSQL.zip

python3.13 -m venv venv/ --prompt .

source venv/bin/activate

cd CData.Python.PostgreSQL/unix

python -m pip install cdata-postgresql-connector-25.0.9376-python3.tar.gz
```

```
Processing ./cdata-postgresql-connector-25.0.9376-python3.tar.gz
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: cdata-postgresql-connector
  Building wheel for cdata-postgresql-connector (pyproject.toml) ... done
  Created wheel for cdata-postgresql-connector: filename=cdata_postgresql_connector-25.0.9376-py3-none-any.whl size=55614110 sha256=0a8de6037deb682a605de41cd48e1adff025ee29e49f077e2c105d2ccb9a0448
  Stored in directory: /home/ubuntu/.cache/pip/wheels/46/5f/52/8d7f94775a1520e77fca4c1e53f2062c245b8066f0fa0eab5d
Successfully built cdata-postgresql-connector
Installing collected packages: cdata-postgresql-connector
Successfully installed cdata-postgresql-connector-25.0.9376
```

```bash
cd venv/lib/python3.13/site-packages/cdata/installlic_postgresql/

./install-license.sh
```

<https://www.postgresql.org/docs/current/sql-copy.html>

```
cut -d, -f 1,4,7 Account.csv > account_columns.csv

ubuntu@LAPTOP-JBell:~/CData.Python.PostgreSQL$ head -n 5 account_columns.csv
Id,Name,BillingStreet
"0016A000003FZabQAG","Edge Communications,""
"0016A00000LSBFMQA5","Zoozzy","7402 Cleveland Ave."
"0016A00000LSBFLQA5","Zooxo","9682 Shady Dr."
"0016A00000LSBFKQA5","Zoovu","107 Green Court"
```

```
postgres=# CREATE TABLE account (
  Id  varchar(255) PRIMARY KEY,
  Name varchar(255),
  BillingStreet varchar(255)
);
CREATE TABLE

postgres=# \copy account FROM '/home/ubuntu/CData.Python.PostgreSQL/account_columns.csv' DELIMITER ',' HEADER CSV
COPY 567

postgres=# SELECT * FROM account LIMIT 5;
         id         |        name         |     billingstreet
--------------------+---------------------+-----------------------
 0016A000003FZabQAG | Edge Communications |
 0016A00000LSBFMQA5 | Zoozzy              | 7402 Cleveland Ave.
 0016A00000LSBFLQA5 | Zooxo               | 9682 Shady Dr.
 0016A00000LSBFKQA5 | Zoovu               | 107 Green Court
 0016A00000LSBFJQA5 | Zooveo              | 94 Bay Meadows Street
(5 rows)
```

```python3
import cdata.postgresql as mod

conn = mod.connect("User=postgres;Password=postgres;Database=postgres;Server=127.0.0.1;Port=5432")

cur = conn.execute("SELECT * FROM account LIMIT 5;")

rs = cur.fetchall()

for row in rs:
    print(row)
```

```
(CData.Python.PostgreSQL) ubuntu@LAPTOP-JBell:~/CData.Python.PostgreSQL$ /home/ubuntu/CData.Python.PostgreSQL/venv/bin/python /home/ubuntu/CData.Python.PostgreSQL/cdata_postgres_connector.py
('0016A000003FZabQAG', 'Edge Communications', '')
('0016A00000LSBFMQA5', 'Zoozzy', '7402 Cleveland Ave.')
('0016A00000LSBFLQA5', 'Zooxo', '9682 Shady Dr.')
('0016A00000LSBFKQA5', 'Zoovu', '107 Green Court')
('0016A00000LSBFJQA5', 'Zooveo', '94 Bay Meadows Street')
```
