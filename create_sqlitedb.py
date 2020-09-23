import csv
import sqlite3

def create_db(file_name):
    '''
    '''

    try:
        conn = sqlite3.connect(file_name)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    else:
        return conn

def create_tables(conn, tables):
    '''
    '''

    create_tables_sql = {}
    create_tables_sql['basics'] = '''
    CREATE TABLE IF NOT EXISTS basics (
        id TEXT UNIQUE PRIMARY KEY,
        type TEXT,
        title TEXT,
        startYear INTEGER,
        endYear INTEGER,
        runtime INTEGER,
        genres TEXT
    );
    '''

    create_tables_sql['episodes'] = '''
    CREATE TABLE IF NOT EXISTS episodes (
        id TEXT UNIQUE PRIMARY KEY,
        parent_id INTEGER,
        season INTEGER,
        episode INTEGER,
        FOREIGN KEY (parent_id) REFERENCES basics (id)
    );
    '''

    create_tables_sql['ratings'] = '''
    CREATE TABLE IF NOT EXISTS ratings (
        id TEXT UNIQUE PRIMARY KEY,
        avgRating REAL,
        numVotes INTEGER
    );
    '''
    
    for table in tables:
        conn.execute(f'DROP TABLE IF EXISTS {table};')

    try:
        for table in tables:
            conn.execute(create_tables_sql[table])
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.commit()

def fill_tables(conn, table):
    '''
    '''

    with open(f'./data/{table}.tsv', newline='') as f_tsv:
        print(f'Opening table {table}.tsv')
        reader = csv.reader(f_tsv, delimiter='\t')
        #Skip the header row but get n_columns
        n_cols = len(next(reader, None))

        #Get column names from table
        get_col_names = conn.execute(f'SELECT * from {table} limit 1')
        col_names = [col[0] for col in get_col_names.description]

        query = f'INSERT INTO {table} (cols) VALUES(' + '?,'*n_cols
        query = query.replace('cols', ','.join(col_names)).rstrip(',') + ')'
        print(query)
        conn.executemany(query, reader)
        conn.commit()

if __name__ == '__main__':

    data_tables = ['basics', 'episodes', 'ratings']

    conn = create_db('./moviegraphs.db')
    create_tables(conn, data_tables)

    for table in data_tables:
        fill_tables(conn, table)

    conn.close()
