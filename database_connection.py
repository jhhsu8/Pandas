import mysql.connector
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(
        host="hostname",
        user="username",
        passwd="password",
        database="database_name"
        )

cursor = cnx.cursor()

df = pd.read_sql_query("SELECT * FROM grips LIMIT 10", cnx)
df.replace([None], "Null", inplace=True)

df