# Step 1: Install PostgreSQL

The install instructions for Linux simply be a matter of following the instructions on the install page on the Postgres website

```
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

# Step 2: Set your password

Once you've install Postgres, you need to set the password for the root user. In your shell,

```
$ psql -h localhost -U postgres
postgres=# \password postgres
(you will be prompted for a password here, just 123 is fine)
```

# Step 3: Create the database

Still in the Postgress command line, enter the following to create your local elbow_bumps database.

```
postgres=# CREATE DATABASE elbow_bumps;
```

Now, exit Postgres by entering `postgres=# \q`

# Step 4: Adjust the local database URI in main.py (Optional)

This step is only if you've set your password differently or have created a database with a different name.

If this is the case, you need to adjust your local database URI in main.py. In the first few lines, look for the lines following `if ENV == 'dev':`,
and changed the string after 
`app.config['SQLALCHEMY_DATABASE_URI'] = ` to follow this format:

```
'postgresql://[postgres username]:[password set earlier]@localhost/[database_name]'
```

If you have followed the previous instructions exactly, the string should be `postgresql://postgres:123@localhost/elbow_bumps`.

# Step 5: Running and testing the local server

First, run `git fetch` and `git pull` in the root directory of this repository to get the latest version.

Once you have done this, you are ready to run the server. If you have not already installed the requirements, run `pip3 install 
flask Flask-SQLAlchemy gunicorn psycopg2-binary vaderSentiment` first, then run `python3 main.py`.

With main.py running, open another tab in your terminal, then enter `curl -X POST http://127.0.0.1:5000/test_user`. Now, to see if this has inserted a row in the 
database, enter in your shell

```
$ psql -h localhost -U postgres
[you will be prompted for your password]
postgres=# \c elbow_bumps
postgres=# SELECT * from user_data;
[The table should be displayed here]
postgres=# \q
```
