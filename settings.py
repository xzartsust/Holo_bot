import dj_database_url
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn= psycopg2.connect(DATABASE_URL, sslmode='require')
DATABASE_URL['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)