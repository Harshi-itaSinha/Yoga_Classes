import psycopg2
from psycopg2 import sql

# Replace these values with your PostgreSQL database credentials
db_params = {
    "host": "dpg-clvjided3nmc738dnvu0-a",
    "database": "yoga_3pkn",
    "user": "yoga_3pkn_user",
    "password": "3r2cqEhJ8H11kMBf6RSVYxG00VtEI381",
    "port":"5432",
}

# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Define the table creation SQL statement
    table_name = "example_table"
    create_table_query = sql.SQL(
        """
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER
        )
        """
    ).format(table_name=sql.Identifier(table_name))

    # Execute the table creation query
    cursor.execute(create_table_query)
    connection.commit()

    print(f"Table '{table_name}' created successfully.")

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
