import sqlite3

def load_data(data, db_name, table_name):
    """
    Function to load the transformed data into a SQLite database.
    :param data: DataFrame containing the transformed data.
    :param db_name: str, name of the SQLite database.
    :param table_name: str, name of the table to insert the data into.
    """
    # TODO: Implement logic to load data into a SQLite database
    try:
        conn = sqlite3.connect(db_name)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
    except Exception as e:
        print(f"Error loading data into database: {e}")
