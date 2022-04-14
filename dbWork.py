import sqlite3
import pandas as pd

#SQlite database connection
new_connection = sqlite3.connect(r'C:\Users\Aasim\Downloads\Applied+Python+Files\Applied Python Files\demo5.db')

# Loading data into DataFrame
demo_data = pd.read_csv('demo5.csv')

# write the data to sqlite table
demo_data.to_sql('demo5', new_connection, if_exists='replace', index=False)

# close connection
new_connection.close()