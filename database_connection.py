import mysql.connector
import pandas as pd
import numpy as np

#database connection
cnx = mysql.connector.connect(
        host="hostname",
        user="username",
        passwd="password",
        database="database_name"
)

#SQL query
df = pd.read_sql_query("""SELECT DISTINCT mouse_name,
                datediff(insulins.datetime, mice.birth_date) / 7 AS mouse_age,
                mice.genotype,
                mice.sex,
                mice.birth_date,
                project_types.name,
                insulins.insulin
FROM insulins
         INNER JOIN mice ON mice.mouse_id = insulins.mouse_name
         INNER JOIN projects ON projects.id = mice.project_id
         INNER JOIN project_types ON project_types.id = projects.project_type_id
WHERE project_types.name IN ('KOMP2', 'K2P2EA')
  AND mice.genotype IN ('Wt', 'Wt-l')
ORDER BY mice.birth_date""", cnx)

#Replace "None" with "NULL"
df.replace([None], "NULL", inplace=True)
df
